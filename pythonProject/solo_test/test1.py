import os
import matplotlib.pyplot as plt
from tensorboard.backend.event_processing.event_accumulator import EventAccumulator
import yaml
from ultralytics import YOLO
import torch

def main():
    # CUDA 설정 확인
    print("CUDA Available:", torch.cuda.is_available())  # True여야 GPU가 사용 가능함을 의미
    if torch.cuda.is_available():
        print("Number of GPUs:", torch.cuda.device_count())  # 사용 가능한 GPU 개수
        print("GPU Name:", torch.cuda.get_device_name(0))  # 첫 번째 GPU 이름

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

    print("Dataset paths are correct. Starting YOLOv10 training...")

    # 사전 학습된 YOLOv10 모델 불러오기
    model = YOLO('yolov10n.pt')  # yolov10n.pt, yolov10s.pt 등 다양한 모델 크기 선택 가능
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

    # TensorBoard 로그 디렉토리 경로
    log_dir = 'runs/detect/train'

    # 로그 파일을 찾는 함수
    def find_log_file(log_dir):
        for root, dirs, files in os.walk(log_dir):
            for file in files:
                if file.startswith('events.out.tfevents'):
                    return os.path.join(root, file)
        return None

    # 로그 파일 경로
    log_file = find_log_file(log_dir)

    # 로그 파일이 존재하는지 확인
    if log_file is None:
        print(f"No TensorBoard log file found in {log_dir}")
    else:
        print(f"Found TensorBoard log file: {log_file}")

        # TensorBoard 로그 데이터 불러오기
        event_acc = EventAccumulator(log_file)
        event_acc.Reload()

        # 로그에서 필요한 값 추출
        epochs = []
        train_loss = []
        val_mAP_50 = []

        # 올바른 키 값을 사용하여 데이터 추출
        for scalar in event_acc.Scalars('train/box_loss'):
            epochs.append(scalar.step)
            train_loss.append(scalar.value)

        for scalar in event_acc.Scalars('metrics/mAP_0.5'):
            val_mAP_50.append(scalar.value)

        # 그래프 그리기
        plt.figure(figsize=(12, 10))

        # Training Losses Plot
        plt.subplot(2, 1, 1)
        plt.plot(epochs, train_loss, label='Train Loss', color='orange')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.title('Training Losses')
        plt.legend()

        # mAP Scores Plot
        plt.subplot(2, 1, 2)
        plt.plot(epochs, val_mAP_50, label='mAP@0.5', color='blue')
        plt.xlabel('Epochs')
        plt.ylabel('mAP')
        plt.title('mAP Scores')
        plt.legend()

        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    main()
