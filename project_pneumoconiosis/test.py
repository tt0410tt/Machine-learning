import torch
import torch.nn as nn
import torch.nn.functional as F

class UNet(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(UNet, self).__init__()
        self.enc1 = self.conv_block(in_channels, 64)
        self.enc2 = self.conv_block(64, 128)
        self.enc3 = self.conv_block(128, 256)
        self.enc4 = self.conv_block(256, 512)
        self.center = self.conv_block(512, 1024)

        self.dec4 = self.up_conv_block(1024, 512)
        self.dec3 = self.up_conv_block(512, 256)
        self.dec2 = self.up_conv_block(256, 128)
        self.dec1 = self.up_conv_block(128, 64)

        self.out = nn.Conv2d(64, out_channels, kernel_size=1)

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
        enc1 = self.enc1(x)
        enc2 = self.enc2(F.max_pool2d(enc1, 2))
        enc3 = self.enc3(F.max_pool2d(enc2, 2))
        enc4 = self.enc4(F.max_pool2d(enc3, 2))
        center = self.center(F.max_pool2d(enc4, 2))

        dec4 = self.dec4(F.interpolate(center, scale_factor=2, mode='bilinear', align_corners=True))
        dec3 = self.dec3(F.interpolate(dec4 + enc4, scale_factor=2, mode='bilinear', align_corners=True))
        dec2 = self.dec2(F.interpolate(dec3 + enc3, scale_factor=2, mode='bilinear', align_corners=True))
        dec1 = self.dec1(F.interpolate(dec2 + enc2, scale_factor=2, mode='bilinear', align_corners=True))

        return self.out(F.interpolate(dec1 + enc1, scale_factor=2, mode='bilinear', align_corners=True))

# 모델 로드
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = UNet(in_channels=3, out_channels=1).to(device)
model.load_state_dict(torch.load('C:/Users/user/Desktop/workspace/main/lung-segmentation-master/models/unet-2v.pt', map_location=device))
model.eval()
