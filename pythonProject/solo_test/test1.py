import os
import shutil

# 원본 이미지 폴더 경로
source_folder = 'dataset/0'
# 복사할 폴더 경로
folder1 = 'dataset/train/no_body'
folder2 = 'dataset/var/no_body'

# 폴더가 없는 경우 생성
os.makedirs(folder1, exist_ok=True)
os.makedirs(folder2, exist_ok=True)

# 모든 파일 읽어오기
all_files = [f for f in os.listdir(source_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]

# 8대 2 비율로 나누기
split_point = int(len(all_files) * 0.8)
files_for_folder1 = all_files[:split_point]
files_for_folder2 = all_files[split_point:]

# 파일 복사 함수
def copy_files(file_list, destination_folder):
    for filename in file_list:
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(destination_folder, filename)
        shutil.copy(src_path, dst_path)

# 파일 복사
copy_files(files_for_folder1, folder1)
copy_files(files_for_folder2, folder2)

print("파일이 성공적으로 나눠져서 복사되었습니다.")