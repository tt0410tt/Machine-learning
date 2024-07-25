import os
import yaml
from ultralytics import YOLO
import torch

def train_model():
    # CUDA 설정 확인
    print("CUDA Available:", torch.cuda.is_available())  # True여야 GPU가 사용 가능함을 의미
    if torch.cuda.is_available():
        print("Number of GPUs:", torch.cuda.device_count())  # 사용 가능한 GPU 개수
        print("GPU Name:", torch.cuda.get_device_name(0))  # 첫 번째 GPU 이름

    data_path = os.path.abspath('dataset')
    train_path = os.path.join(data_path, 'images', 'train')
    val_path = os.path.join(data_path, 'images', 'val')

    # Ultralytics 설정 초기화
    ultralytics_config_path = os.path.join(os.getenv('APPDATA'), 'Ultralytics', 'settings.yaml')
    if os.path.exists(ultralytics_config_path):
        os.remove(ultralytics_config_path)
        print(f"Removed existing Ultralytics settings: {ultralytics_config_path}")

    # 학습을 위한 데이터셋 구성 파일 작성 (이미 작성된 경우는 스킵 가능)
    data_config = {
        'train': train_path,
        'val': val_path,
        'nc': 1,
        'names': ['face']
    }

    # 데이터셋 구성 파일 저장
    dataset_yaml_path = os.path.join(data_path, 'dataset.yaml')
    with open(dataset_yaml_path, 'w') as f:
        yaml.dump(data_config, f)

    print("Dataset paths are correct. Starting YOLOv8 training...")

    # 사전 학습된 YOLOv8 모델 불러오기
    model = YOLO('yolov8n.pt')  # yolov8n.pt, yolov8s.pt 등 다양한 모델 크기 선택 가능
    # 모델 학습
    print("Training the model...")
    model.train(data=dataset_yaml_path, epochs=100, imgsz=640, device='cuda' if torch.cuda.is_available() else 'cpu')

    # 모델 평가
    print("Evaluating the model...")
    results = model.val()

    # 학습된 모델 저장
    model_save_path = os.path.abspath('save_model.pt')
    model.save(model_save_path)

    print(f"Model saved to {model_save_path}")

if __name__ == '__main__':
    train_model()
