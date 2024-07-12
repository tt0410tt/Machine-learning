import os
import torchvision.transforms as transforms
from PIL import Image
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

# U-Net 모델 정의
class UNet(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(UNet, self).__init__()
        self.encoder1 = self.conv_block(in_channels, 64)
        self.encoder2 = self.conv_block(64, 128)
        self.encoder3 = self.conv_block(128, 256)
        self.encoder4 = self.conv_block(256, 512)
        self.encoder5 = self.conv_block(512, 1024)

        self.decoder1 = self.up_conv_block(1024, 512)
        self.decoder2 = self.up_conv_block(512, 256)
        self.decoder3 = self.up_conv_block(256, 128)
        self.decoder4 = self.up_conv_block(128, 64)

        self.final_layer = nn.Conv2d(64, out_channels, kernel_size=1)

    def conv_block(self, in_channels, out_channels):
        return nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1),
            nn.ReLU(inplace=True)
        )

    def up_conv_block(self, in_channels, out_channels):
        return nn.Sequential(
            nn.ConvTranspose2d(in_channels, out_channels, kernel_size=2, stride=2),
            nn.ReLU(inplace=True),
            self.conv_block(out_channels, out_channels)
        )

    def forward(self, x):
        enc1 = self.encoder1(x)
        enc2 = self.encoder2(F.max_pool2d(enc1, 2))
        enc3 = self.encoder3(F.max_pool2d(enc2, 2))
        enc4 = self.encoder4(F.max_pool2d(enc3, 2))
        enc5 = self.encoder5(F.max_pool2d(enc4, 2))

        dec1 = self.decoder1(F.interpolate(enc5, scale_factor=2, mode='bilinear', align_corners=True))
        dec2 = self.decoder2(F.interpolate(dec1 + enc4, scale_factor=2, mode='bilinear', align_corners=True))
        dec3 = self.decoder3(F.interpolate(dec2 + enc3, scale_factor=2, mode='bilinear', align_corners=True))
        dec4 = self.decoder4(F.interpolate(dec3 + enc2, scale_factor=2, mode='bilinear', align_corners=True))

        return self.final_layer(F.interpolate(dec4 + enc1, scale_factor=2, mode='bilinear', align_corners=True))

# 모델 로드
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = UNet(in_channels=3, out_channels=1).to(device)
model.load_state_dict(torch.load('C:/Users/user/Desktop/workspace/main/lung-segmentation-master/models/unet-2v.pt', map_location=device))
model.eval()

# 이미지 및 마스크 전처리
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor()
])

# 마스크 생성 및 저장 함수
def generate_mask(image_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    image_filenames = os.listdir(image_folder)
    
    for img_name in image_filenames:
        img_path = os.path.join(image_folder, img_name)
        image = Image.open(img_path).convert('RGB')
        image = transform(image).unsqueeze(0).to(device)

        with torch.no_grad():
            output = model(image)
            mask = torch.sigmoid(output).squeeze().cpu().numpy()
            mask = (mask > 0.5).astype(np.uint8) * 255
            mask = Image.fromarray(mask)

            base_name = os.path.splitext(img_name)[0]
            output_path = os.path.join(output_folder, f"{base_name}_MASK.png")
            mask.save(output_path)
            print(f"Saved mask to {output_path}")

# 경로 설정 및 함수 호출
base_path = 'C:/Users/user/Desktop/workspace/main/data_pneumoconiosis'
folders = [
    'test/NORMAL',
    'test/PNEUMONIA',
    'train/NORMAL',
    'train/PNEUMONIA',
    'val/NORMAL',
    'val/PNEUMONIA'
]

output_folders = [
    'test/NORMAL_MASK',
    'test/PNEUMONIA_MASK',
    'train/NORMAL_MASK',
    'train/PNEUMONIA_MASK',
    'val/NORMAL_MASK',
    'val/PNEUMONIA_MASK'
]

for image_subfolder, output_subfolder in zip(folders, output_folders):
    image_folder = os.path.join(base_path, image_subfolder).replace('\\', '/')
    output_folder = os.path.join(base_path, output_subfolder).replace('\\', '/')
    print(f"Processing folder: {image_folder}")
    generate_mask(image_folder, output_folder)
