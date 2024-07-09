import os
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
from PIL import Image

# 데이터셋 경로 설정
data_path = ''
train_normal_path = os.path.join(data_path, 'train/NORMAL')
train_pneumonia_path = os.path.join(data_path, 'train/PNEUMONIA')
test_normal_path = os.path.join(data_path, 'test/NORMAL')
test_pneumonia_path = os.path.join(data_path, 'test/PNEUMONIA')
val_normal_path = os.path.join(data_path, 'val/NORMAL')
val_pneumonia_path = os.path.join(data_path, 'val/PNEUMONIA')

# 이미지 전처리
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor()
])

# 이미지 로드 및 전처리 함수
def load_images_from_folder(folder, num_images=2):
    images = []
    print(folder)
    for idx, filename in enumerate(os.listdir(folder)):
        if idx >= num_images:
            break
        img_path = os.path.join(folder, filename)
        img = Image.open(img_path).convert('RGB')
        img = transform(img)
        images.append(img)
    return images

# 이미지 로드
train_normal_images = load_images_from_folder(train_normal_path)
train_pneumonia_images = load_images_from_folder(train_pneumonia_path)
test_normal_images = load_images_from_folder(test_normal_path)
test_pneumonia_images = load_images_from_folder(test_pneumonia_path)
val_normal_images = load_images_from_folder(val_normal_path)
val_pneumonia_images = load_images_from_folder(val_pneumonia_path)

# 이미지 시각화
def plot_images(images, title):
    fig, axes = plt.subplots(1, len(images), figsize=(15, 5))
    fig.suptitle(title)
    for idx, img in enumerate(images):
        img = img.permute(1, 2, 0)  # 채널 차원 변경
        axes[idx].imshow(img)
        axes[idx].axis('off')
    plt.show()

plot_images(train_normal_images, 'Train Normal Images')
plot_images(train_pneumonia_images, 'Train Pneumonia Images')
plot_images(test_normal_images, 'Test Normal Images')
plot_images(test_pneumonia_images, 'Test Pneumonia Images')
plot_images(val_normal_images, 'Val Normal Images')
plot_images(val_pneumonia_images, 'Val Pneumonia Images')

"""
train_dataset = datasets.ImageFolder(train_path, transform=transform)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

test_dataset = datasets.ImageFolder(test_path, transform=transform)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

# 모델 정의
class CNNModel(nn.Module):
    def __init__(self):
        super(CNNModel, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.conv4 = nn.Conv2d(128, 128, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(128 * 16 * 16, 512)
        self.fc2 = nn.Linear(512, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = self.pool(torch.relu(self.conv3(x)))
        x = self.pool(torch.relu(self.conv4(x)))
        x = x.view(-1, 128 * 16 * 16)
        x = torch.relu(self.fc1(x))
        x = self.sigmoid(self.fc2(x))
        return x

model = CNNModel()

# 손실 함수 및 옵티마이저 정의
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 모델 학습
num_epochs = 10
for epoch in range(num_epochs):
    for images, labels in train_loader:
        labels = labels.view(-1, 1).float()
        outputs = model(images)
        loss = criterion(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# 모델 평가
model.eval()
with torch.no_grad():
    correct = 0
    total = 0
    for images, labels in test_loader:
        labels = labels.view(-1, 1).float()
        outputs = model(images)
        predicted = (outputs > 0.5).float()
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    print(f'Accuracy: {100 * correct / total:.2f}%')
    """