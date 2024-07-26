from ultralytics import YOLO

# 기존 모델 로드
model_path = 'save_model.pt'
model = YOLO(model_path)

# 모델 재학습
model.train(data='data.yaml', epochs=10)

# 새로운 모델 저장
model.save('retrained_model.pt')
print("Model retraining completed and saved as 'retrained_model.pt'")
