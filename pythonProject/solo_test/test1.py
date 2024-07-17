import cv2
import torch
from ultralytics import YOLO

# YOLOv8 모델 불러오기
model = YOLO('yolov8x.pt')  # 적절한 가중치 파일 경로를 입력하세요

# 이미지 불러오기
image_path = 'path/to/your/image.jpg'  # 이미지 파일 경로를 입력하세요
image = cv2.imread(image_path)

# 모델을 사용하여 객체 탐지
results = model(image)

# 결과를 이미지에 그리기
for result in results:
    boxes = result.boxes  # 탐지된 객체의 바운딩 박스
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]  # 바운딩 박스 좌표
        label = box.cls  # 클래스 라벨
        conf = box.conf  # 신뢰도

        # 바운딩 박스 그리기
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(image, f'{label} {conf:.2f}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# 결과 이미지 저장
output_path = 'path/to/save/detected_image.jpg'  # 결과 이미지를 저장할 경로를 입력하세요
cv2.imwrite(output_path, image)

# 결과 이미지 보여주기
cv2.imshow('YOLOv8 Full Body Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()