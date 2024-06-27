import cv2
import os
import time

# 데이터셋 저장 디렉토리 설정
dataset_dir = "dataset"
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)

# 웹캠 설정
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        # 여백을 추가하여 얼굴 주변의 더 큰 영역을 캡처
        padding = 20  # 여백 크기
        x1 = max(0, x - padding)
        y1 = max(0, y - padding)
        x2 = min(frame.shape[1], x + w + padding)
        y2 = min(frame.shape[0], y + h + padding)

        # 얼굴 영역 추출
        face = frame[y1:y2, x1:x2]
        # 얼굴 이미지 저장
        face_filename = os.path.join(dataset_dir, f"face_{count}.jpg")
        cv2.imwrite(face_filename, face)
        count += 1

        # 화면에 얼굴 바운딩 박스 표시
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    cv2.imshow('Webcam Face Capture', frame)

    # 1초 대기
    time.sleep(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

