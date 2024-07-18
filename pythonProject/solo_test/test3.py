import os
import matplotlib.pyplot as plt
from tensorboard.backend.event_processing.event_accumulator import EventAccumulator

# TensorBoard 로그 디렉토리 경로
log_dir = 'runs/detect/train15'

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

    # 사용 가능한 모든 키 출력
    tags = event_acc.Tags()['scalars']
    print("Available tags:", tags)

    # 여기서 올바른 키를 사용하여 데이터를 추출합니다
    epochs = []
    box_loss = []
    obj_loss = []
    val_mAP_50 = []
    val_mAP_50_95 = []

    # 올바른 키 값을 사용하여 데이터 추출
    for scalar in event_acc.Scalars('train/box_loss'):
        epochs.append(scalar.step)
        box_loss.append(scalar.value)
    
    for scalar in event_acc.Scalars('train/obj_loss'):
        obj_loss.append(scalar.value)
    
    for scalar in event_acc.Scalars('metrics/mAP_0.5'):
        val_mAP_50.append(scalar.value)
    
    for scalar in event_acc.Scalars('metrics/mAP_0.5:0.95'):
        val_mAP_50_95.append(scalar.value)

    # 그래프 그리기
    plt.figure(figsize=(12, 10))

    # Training Losses Plot
    plt.subplot(2, 1, 1)
    plt.plot(epochs, box_loss, label='Box Loss', color='orange')
    plt.plot(epochs, obj_loss, label='Objectness Loss', color='blue')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Training Losses')
    plt.legend()

    # mAP Scores Plot
    plt.subplot(2, 1, 2)
    plt.plot(epochs, val_mAP_50, label='mAP@0.5', color='blue')
    plt.plot(epochs, val_mAP_50_95, label='mAP@0.5:0.95', color='orange')
    plt.xlabel('Epochs')
    plt.ylabel('mAP')
    plt.title('mAP Scores')
    plt.legend()

    plt.tight_layout()
    plt.show()
