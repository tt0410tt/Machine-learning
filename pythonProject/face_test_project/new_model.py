import os
from ultralytics import YOLO

# YOLO 모델 로드
model_path = 'save_model.pt'  # 기존 학습된 모델 경로
model = YOLO(model_path)

# 데이터셋 디렉터리 설정
dataset_dir = 'C:/Users/user/Desktop/workspace/main/Machine-learning/pythonProject/face_test_project/save_data/person1'

# 학습용 데이터셋 준비
train_dir = os.path.join(dataset_dir, 'train')
val_dir = os.path.join(dataset_dir, 'val')

# 데이터셋 구성
data_yaml_content = f"""
names:
  - person1
  - other
nc: 2
train: {train_dir}
val: {val_dir}
"""

# 데이터셋 YAML 파일 생성
with open('data.yaml', 'w') as file:
    file.write(data_yaml_content)

# 추가 학습 수행
model.train(data='data.yaml', epochs=10, name='custom_model', save_period=1, resume=True)
