import cv2
import torch
from ultralytics import YOLO

# YOLO 모델 로드
model_path = 'save_model.pt'  # 저장된 모델 경로
model = YOLO(model_path)

# 이미지 파일 경로
image_path = '0.jpg'

# 이미지 읽기
image = cv2.imread(image_path)
if image is None:
    print("Error: Unable to read image file.")
    exit()

# 모델로 예측 수행
results = model(image)

# 얼굴 인식 결과를 이미지에 표시
for result in results[0].boxes:
    x1, y1, x2, y2 = map(int, result.xyxy[0])
    confidence = result.conf[0]

    # 얼굴 인식 사각형 그리기
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 인식률 텍스트 추가
    text = f"{confidence:.2f}"
    cv2.putText(image, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# 결과 이미지 저장
output_path = 'detected_faces.jpg'
cv2.imwrite(output_path, image)
print(f"Face detection image saved as {output_path}")
