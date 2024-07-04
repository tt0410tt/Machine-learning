from pyimagesearch.localbinarypatterns import LocalBinaryPatterns
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from imutils import paths
import argparse
import cv2
import os

# 명령줄 인자 파서를 설정합니다.
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--training", required=True, help="path to the training images")
ap.add_argument("-e", "--testing", required=True, help="path to the testing images")
args = vars(ap.parse_args())

# Local Binary Patterns 설명자를 초기화합니다.
desc = LocalBinaryPatterns(24, 8)
data = []
labels = []

# 학습 이미지를 순회합니다.
for imagePath in paths.list_images(args["training"]):
    image = cv2.imread(imagePath)
    if image is None:
        print(f"Warning: {imagePath} could not be loaded.")
        continue
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    labels.append(imagePath.split(os.path.sep)[-2])  # 디렉토리 이름에서 클래스를 추출합니다.
    data.append(hist)

# 데이터를 정규화합니다.
scaler = StandardScaler()
data = scaler.fit_transform(data)

# 로드된 클래스 수를 확인합니다.
unique_labels = set(labels)
print(f"Unique labels found: {unique_labels}")
if len(unique_labels) < 2:
    raise ValueError("Need at least two different classes for training.")

# Linear SVM을 학습시킵니다.
model = LinearSVC(C=1.0, random_state=42, max_iter=20000)  # max_iter 값을 더 증가시킴
model.fit(data, labels)

# 테스트 이미지를 순회합니다.
for imagePath in paths.list_images(args["testing"]):
    image = cv2.imread(imagePath)
    if image is None:
        print(f"Warning: {imagePath} could not be loaded.")
        continue
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    hist = scaler.transform([hist])  # 테스트 데이터도 정규화합니다.
    prediction = model.predict(hist.reshape(1, -1))

    # 이미지와 예측 결과를 표시합니다.
    cv2.putText(image, prediction[0], (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
    cv2.imshow("Image", image)
    cv2.waitKey(0)