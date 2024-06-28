# 필요한 모듈을 불러들입니다.
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 세트의 파일 경로를 설정 (절대경로)
file_path = "C:/Users/user/Desktop/workspace/main/Machine-learning/2024_06_28_test/Diabetes/diabetes.csv"
# 상대경로
file_path = "./Diabetes/diabetes.csv"

# 재현성을 위해 random seed 설정
np.random.seed(2)

# 데이터 세트를 불러옵니다.
data = pd.read_csv(file_path)

# 데이터세트를 두 가지 원인(X) 과 결과(Y)로 나누어 줍니다.
X = data.iloc[:, 0:8].values
Y = data.iloc[:, 8].values

# 모델 만들기
model = Sequential()
model.add(Dense(12, input_dim=8, activation="relu"))  # 입력층은 input_dim 매개변수가 필요합니다.
model.add(Dense(15, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(10, activation="relu"))
model.add(Dense(1, activation="sigmoid"))  # 최종 확률을 0과 1 사이로 하기 위해 sigmoid 사용

# 모델 컴파일, adam 최적화 알고리즘 사용
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# 데이터를 학습합니다. (네트워크 훈련)
# verbose=0 은 진행 상황을 숨깁니다.
history = model.fit(X, Y, epochs=800, batch_size=10, verbose=0)

# 모델의 정확도를 계산합니다.
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

# 그래프 그리기
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=False, figsize=(10, 5))

# 모델의 정확도 그래프
ax0.plot(history.history["accuracy"])
ax0.set(title="모델 정확도", xlabel="에포크", ylabel="정확도")

# 모델의 오차 그래프
ax1.plot(history.history["loss"])
ax1.set(title="모델 오차", xlabel="에포크", ylabel="오차")

# 가상의 환자 데이터 입력
patient_1 = np.array([[0, 137, 90, 35, 168, 43.1, 2.288, 33]])

# 모델로 예측하기
prediction = model.predict(patient_1)

# 예측결과 출력하기
print(prediction * 100)

plt.show()