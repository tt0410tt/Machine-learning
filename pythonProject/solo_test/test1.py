import os
import random
import shutil
import matplotlib.pyplot as plt
import yaml
from ultralytics import YOLO

# 데이터셋 경로 설정 (절대 경로 사용)
data_path = os.path.abspath('dataset')

# Ultralytics 설정 초기화
ultralytics_config_path = os.path.join(os.getenv('APPDATA'), 'Ultralytics', 'settings.yaml')
if os.path.exists(ultralytics_config_path):
    os.remove(ultralytics_config_path)
    print(f"Removed existing Ultralytics settings: {ultralytics_config_path}")

# 학습을 위한 데이터셋 구성 파일 작성 (이미 작성된 경우는 스킵 가능)
data_config = {
    'train': os.path.join(data_path, 'images', 'train'),
    'val': os.path.join(data_path, 'images', 'val'),
    'nc': 1,
    'names': ['full_body']
}

# 데이터셋 구성 파일 저장
dataset_yaml_path = os.path.join(data_path, 'dataset.yaml')
with open(dataset_yaml_path, 'w') as f:
    yaml.dump(data_config, f)

print("Dataset paths are correct. Starting YOLOv8 training...")

# 사전 학습된 YOLOv8 모델 불러오기
model = YOLO('yolov8x.pt')  # yolov8n.pt, yolov8s.pt 등 다양한 모델 크기 선택 가능

# 모델 학습
print("Training the model...")
model.train(data=dataset_yaml_path, epochs=5, imgsz=640)

# 모델 평가
print("Evaluating the model...")
results = model.val()

# 학습된 모델 저장
model_save_path = os.path.abspath('save_model.pt')
model.save(model_save_path)

print(f"Model saved to {model_save_path}")

# 학습 로그 파일 경로
log_file_path = os.path.join('runs', 'detect', 'train', 'results.txt')

# 로그 파일에서 데이터를 읽어 그래프를 그리는 함수
def plot_training_log(log_file_path):
    epochs = []
    train_loss = []
    val_mAP = []

    with open(log_file_path, 'r') as f:
        for line in f:
            if 'Epoch' in line:
                parts = line.split()
                epochs.append(int(parts[1].strip(',')))
                train_loss.append(float(parts[5].strip(',')))
                val_mAP.append(float(parts[7].strip(',')))

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(epochs, train_loss, label='Train Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Train Loss over Epochs')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(epochs, val_mAP, label='Validation mAP@50')
    plt.xlabel('Epoch')
    plt.ylabel('mAP@50')
    plt.title('Validation mAP@50 over Epochs')
    plt.legend()

    plt.tight_layout()
    plt.show()

# 로그 파일에서 데이터를 읽어 그래프 그리기
plot_training_log(log_file_path)
