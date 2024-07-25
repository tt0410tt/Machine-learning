import cv2
import torch
import numpy as np
from ultralytics import YOLO
from scipy.ndimage import label
import random

# 모델 로드
model_path = 'save_model.pt'
model = YOLO(model_path)

# 카메라 캡처 시작
cap = cv2.VideoCapture(0)

while True:
    # 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break

    # 이미지 전처리 - CLAHE 적용
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_image = clahe.apply(gray_image)

    # 모델로 예측 수행
    results = model(frame[..., :3])

    # 얼굴 외곽선을 그리기 위해 빈 이미지 생성
    output_image = np.zeros((frame.shape[0], frame.shape[1], 4), dtype=np.uint8)
    final_output = np.zeros((frame.shape[0], frame.shape[1], 4), dtype=np.uint8)

    # 얼굴 부분만 추출 및 외곽선 검출
    for i, result in enumerate(results[0].boxes):
        x1, y1, x2, y2 = map(int, result.xyxy[0])

        # 각 좌표를 10% 확장
        width = x2 - x1
        height = y2 - y1
        x1 = max(0, x1 - int(0.1 * width))
        y1 = max(0, y1 - int(0.1 * height))
        x2 = min(frame.shape[1], x2 + int(0.1 * width))
        y2 = min(frame.shape[0], y2 + int(0.1 * height))

        face_image = enhanced_image[y1:y2, x1:x2]

        # 외곽선 추출
        edges = cv2.Canny(face_image, 30, 100)  # 민감도 조정

        # 검출된 외곽선을 원본 이미지에 복사
        output_image[y1:y2, x1:x2, 0] = edges
        output_image[y1:y2, x1:x2, 1] = edges
        output_image[y1:y2, x1:x2, 2] = edges
        output_image[y1:y2, x1:x2, 3] = 255

    # 색상 변경 및 카운터 설정
    color_list = []
    stack = []
    counter = 0

    # 비트 검출 및 색상 변경
    h, w = output_image.shape[:2]
    for y in range(h):
        for x in range(w):
            if (output_image[y, x] == [0, 0, 0, 255]).all():  # 검정색이면
                new_color = [random.randint(0, 255) for _ in range(3)] + [255]
                while new_color in color_list:
                    new_color = [random.randint(0, 255) for _ in range(3)] + [255]
                color_list.append(new_color)
                stack.append((x, y))
                counter += 1

                while stack:
                    cx, cy = stack.pop()
                    if 0 <= cx < w and 0 <= cy < h and (output_image[cy, cx] == [0, 0, 0, 255]).all():
                        output_image[cy, cx] = new_color
                        # 인접 비트를 스택에 추가
                        stack.extend([(cx + dx, cy + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]])

    # 노란색 사각형 그리기 및 내부 색상 조사
    unique_colors = set()
    for i, result in enumerate(results[0].boxes):
        x1, y1, x2, y2 = map(int, result.xyxy[0])
        width = x2 - x1
        height = y2 - y1

        # 65% 크기의 사각형 계산
        new_width = int(width * 0.65)
        new_height = int(height * 0.65)
        new_x1 = x1 + (width - new_width) // 2
        new_y1 = y1 + (height - new_height) // 2
        new_x2 = new_x1 + new_width
        new_y2 = new_y1 + new_height
        cv2.rectangle(output_image, (new_x1, new_y1), (new_x2, new_y2), (255, 255, 0, 255), 2)

        # 노란색 사각형 내부의 색상 조사 (흰색 제외)
        for y in range(new_y1, new_y2):
            for x in range(new_x1, new_x2):
                if not (output_image[y, x] == [255, 255, 255, 255]).all():
                    unique_colors.add(tuple(output_image[y, x]))

    # 색상 매핑 및 근처 픽셀 값 확인
    for y in range(h):
        for x in range(w):
            if (output_image[y, x] == [255, 255, 255, 255]).all() or tuple(output_image[y, x]) in unique_colors:
                final_output[y, x] = [255, 255, 255, 255]  # 흰색
            else:
                neighbors = output_image[max(0, y-1):min(h, y+2), max(0, x-1):min(w, x+2)]
                if np.mean(neighbors == [255, 255, 255, 255]) > 0.5:
                    final_output[y, x] = [255, 255, 255, 255]  # 흰색
                else:
                    final_output[y, x] = [0, 0, 0, 255]  # 검정색

    # 연결된 성분 레이블링을 사용하여 작은 흰색 영역 제거
    labeled_array, num_features = label(final_output[..., 0] == 255)
    component_sizes = np.bincount(labeled_array.ravel())
    # 영역이 작으면 검정색으로 변경
    too_small = component_sizes < 500  # 임계값 설정 (기존 100에서 500으로 증가)
    too_small_mask = too_small[labeled_array]
    final_output[too_small_mask] = [0, 0, 0, 255]

    # 결과 이미지 출력
    cv2.imshow('Edge Detection', final_output[..., 0])

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 캡처 종료 및 창 닫기
cap.release()
cv2.destroyAllWindows()
