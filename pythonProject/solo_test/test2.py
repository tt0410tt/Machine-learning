import os
import random
import shutil

# 데이터셋 경로 설정 (절대 경로 사용)
data_path = os.path.abspath('dataset')

# 필요할 폴더 생성
os.makedirs(os.path.join(data_path, 'images', 'train_unused'), exist_ok=True)
os.makedirs(os.path.join(data_path, 'images', 'val_unused'), exist_ok=True)
os.makedirs(os.path.join(data_path, 'labels', 'train_unused'), exist_ok=True)
os.makedirs(os.path.join(data_path, 'labels', 'val_unused'), exist_ok=True)

# 폴더의 파일 목록을 지정된 수로 제한하고 나머지를 이동하는 함수
def select_and_move_files(img_dir, label_dir, num_samples, split):
    img_files = os.listdir(img_dir)
    if len(img_files) > num_samples:
        selected_imgs = random.sample(img_files, num_samples)
        for img_file in img_files:
            label_file = img_file.replace('.jpg', '.txt')
            if img_file not in selected_imgs:
                # 이미지 파일 이동
                shutil.move(os.path.join(img_dir, img_file), os.path.join(data_path, 'images', f'{split}_unused', img_file))
                # 라벨 파일 이동
                shutil.move(os.path.join(label_dir, label_file), os.path.join(data_path, 'labels', f'{split}_unused', label_file))

# 트레인 및 발리데이션 데이터셋에서 지정된 수만 남기고 나머지 이동
select_and_move_files(os.path.join(data_path, 'images', 'train'), os.path.join(data_path, 'labels', 'train'), 50, 'train')
select_and_move_files(os.path.join(data_path, 'images', 'val'), os.path.join(data_path, 'labels', 'val'), 10, 'val')

print("Files selected and moved successfully.")
