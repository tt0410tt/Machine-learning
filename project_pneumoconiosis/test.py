import os
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt

# 데이터셋 경로 설정
data_path = '../../data_pneumoconiosis/images'
mask_path = '../../data_pneumoconiosis/masks'

# 이미지 및 마스크 전처리
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor()
])

# 이미지 및 마스크 로드 및 전처리 함수
def load_images_and_masks(image_folder, mask_folder, num_images=2):
    images = []
    masks = []
    for idx, filename in enumerate(os.listdir(image_folder)):
        if idx >= num_images:
            break
        img_path = os.path.join(image_folder, filename)
        mask_filename = filename.replace('.png', '_mask.png')
        mask_path = os.path.join(mask_folder, mask_filename)
        if not os.path.exists(mask_path):
            print(f"Mask not found for {filename}")
            continue
        img = Image.open(img_path).convert('RGB')
        mask = Image.open(mask_path).convert('L')  # 마스크는 흑백 이미지
        img = transform(img)
        mask = transform(mask)
        images.append(img)
        masks.append(mask)
    return images, masks

# 이미지와 마스크 로드
images, masks = load_images_and_masks(data_path, mask_path)

# 이미지와 마스크를 결합하여 폐 부분만 남기기
def apply_masks(images, masks):
    masked_images = []
    for img, mask in zip(images, masks):
        mask = mask > 0.5  # 마스크 이진화
        masked_img = img * mask  # 마스크 적용
        masked_images.append(masked_img)
    return masked_images

masked_images = apply_masks(images, masks)

# 이미지 시각화
def plot_images(images, title):
    fig, axes = plt.subplots(1, len(images), figsize=(15, 5))
    fig.suptitle(title)
    for idx, img in enumerate(images):
        img = img.permute(1, 2, 0)  # 채널 차원 변경
        axes[idx].imshow(img)
        axes[idx].axis('off')
    plt.show()

# 마스크가 적용된 이미지 확인
plot_images(masked_images, 'Masked Images')
print(len(images))