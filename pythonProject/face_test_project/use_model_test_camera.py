import cv2
import torch
from ultralytics import YOLO

# YOLO 모델 로드
model_path = 'save_model.pt'  # 저장된 모델 경로
model = YOLO(model_path)

# 카메라 캡처 시작
cap = cv2.VideoCapture(0)

while True:
    # 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break

    # 모델로 예측 수행
    results = model(frame)

    # 얼굴 인식 결과를 이미지에 표시
    for result in results[0].boxes:
        x1, y1, x2, y2 = map(int, result.xyxy[0])
        confidence = result.conf[0]

        # 얼굴 인식 사각형 그리기
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # 인식률 텍스트 추가
        text = f"{confidence:.2f}"
        cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # 결과 프레임 출력
    cv2.imshow('Face Detection', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 캡처 종료 및 창 닫기
cap.release()
cv2.destroyAllWindows()
