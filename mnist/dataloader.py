import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Define the transformation: convert to tensor and normalize
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # Normalize the images
])

# Load the training and test datasets
train_data = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_data = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

# Create DataLoader for both train and test datasets
train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
test_loader = DataLoader(test_data, batch_size=64, shuffle=False)

# Example: Print details of the first batch in the training set
for images, labels in train_loader:
    print(f'Batch size: {images.size(0)}')
    print(f'Image shape: {images.shape}')
    print(f'Labels shape: {labels.shape}')
    break  # Only print the first batch
