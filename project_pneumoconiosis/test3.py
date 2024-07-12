import torch

checkpoint = torch.load('C:/Users/user/Desktop/workspace/main/lung-segmentation-master/models/unet-2v.pt', map_location='cpu')
for k in checkpoint.keys():
    print(k)