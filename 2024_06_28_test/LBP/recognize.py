from pyimagesearch.localbinarypatterns import LocalBinaryPatterns
from sklearn.svm import LinearSVC
from imutils import paths
import argparse
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--training", required=True, help="C:/Users/user/Desktop/workspace/main/Machine-learning/2024_06_28_test/LBP/images/training")
ap.add_argument("-e", "--testing", required=True, help="C:/Users/user/Desktop/workspace/main/Machine-learning/2024_06_28_test/LBP/images/testing")
args = vars(ap.parse_args())

desc = LocalBinaryPatterns(24, 8)
data = []
labels = []

# 학습 이미지를 순회합니다.
for imagePath in paths.list_images(args["training"]):
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    labels.append(imagePath.split(os.path.sep)[-2])
    data.append(hist)

# Linear SVM을 학습시킵니다.
model = LinearSVC(C=100.0, random_state=42)
model.fit(data, labels)

# 테스트 이미지를 순회합니다.
for imagePath in paths.list_images(args["testing"]):
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))

    # 이미지와 예측 결과를 표시합니다.
    cv2.putText(image, prediction[0], (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

