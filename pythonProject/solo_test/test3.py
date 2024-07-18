import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import cv2
import numpy as np

# 모델 정의 및 수정 (로드와 동일하게 정의)
model_ft = models.resnet18()
num_ftrs = model_ft.fc.in_features
model_ft.fc = nn.Linear(num_ftrs, 1)  # 출력 클래스 수를 2로 설정 (사람 있음 / 없음)

# 모델 로드
model_ft.load_state_dict(torch.load('person_detection_model.pth'))
model_ft.eval()  # 평가 모드로 설정

# 디바이스 설정
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model_ft = model_ft.to(device)

# 이미지 전처리
def preprocess_image(image):
    input_transforms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    image = Image.fromarray(image)
    image = input_transforms(image).unsqueeze(0)
    return image

# 이미지 슬라이딩 윈도우 및 예측
def sliding_window(image, model, window_size, step_size):
    boxes = []
    img_height, img_width, _ = image.shape

    for y in range(0, img_height - window_size[1] + 1, step_size):
        for x in range(0, img_width - window_size[0] + 1, step_size):
            window = image[y:y + window_size[1], x:x + window_size[0]]
            window_tensor = preprocess_image(window).to(device)

            with torch.no_grad():
                outputs = model(window_tensor)
                _, preds = torch.max(outputs, 1)

            if preds.item() == 0:  # 사람 클래스
                boxes.append((x, y, x + window_size[0], y + window_size[1]))

    return boxes

# 결과 시각화
def visualize_prediction(image_path, boxes):
    image = cv2.imread(image_path)
    for (x1, y1, x2, y2) in boxes:
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, 'Person', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    cv2.imshow('Prediction', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('detected_image.jpg', image)

# 테스트 이미지 경로
test_image_path = 'test.jpg'

# 이미지 로드
image = cv2.imread(test_image_path)

# 사람 검출 및 바운딩 박스 그리기
window_size = (128, 128)  # 슬라이딩 윈도우 크기
step_size = 32  # 슬라이딩 윈도우 이동 간격
boxes = sliding_window(image, model_ft, window_size, step_size)

# 결과 시각화
visualize_prediction(test_image_path, boxes)
