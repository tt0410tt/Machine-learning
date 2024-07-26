import cv2
import os
from ultralytics import YOLO

# YOLO 모델 로드
model_path = 'save_model.pt'  # 저장된 모델 경로
model = YOLO(model_path)

# 저장 디렉터리 설정
save_dir = 'save_data/person1'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 카메라 캡처 시작
cap = cv2.VideoCapture(0)
image_count = 0

def save_label(file_path, x1, y1, x2, y2, img_width, img_height):
    # YOLO 형식으로 변환
    x_center = (x1 + x2) / 2 / img_width
    y_center = (y1 + y2) / 2 / img_height
    width = (x2 - x1) / img_width
    height = (y2 - y1) / img_height

    # 라벨 파일 저장
    with open(file_path, 'w') as file:
        file.write(f"0 {x_center} {y_center} {width} {height}\n")

while True:
    # 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break

    # 모델로 예측 수행
    results = model(frame)

    # 이미지 크기
    img_height, img_width, _ = frame.shape

    # 얼굴 인식 결과를 이미지에 표시
    for result in results[0].boxes:
        x1, y1, x2, y2 = map(int, result.xyxy[0])
        confidence = result.conf[0]

        # 얼굴 부분 추출
        face_image = frame[y1:y2, x1:x2]
        # 이미지 카운터 증가
        image_count += 1

        # 라벨 파일 저장
        label_filename = os.path.join(save_dir, f'face_{image_count}.txt')
        save_label(label_filename, x1, y1, x2, y2, img_width, img_height)
        print(f"Saved {label_filename}")

        # 얼굴 인식 사각형 그리기
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # 인식률 텍스트 추가
        text = f"{confidence:.2f}"
        cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # 전체 이미지 저장
    full_image_filename = os.path.join(save_dir, f'face_{image_count}.jpg')
    cv2.imwrite(full_image_filename, frame)
    print(f"Saved {full_image_filename}")

    # 결과 프레임 출력
    cv2.imshow('Face Detection', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 캡처 종료 및 창 닫기
cap.release()
cv2.destroyAllWindows()
