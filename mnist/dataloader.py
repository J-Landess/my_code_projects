# Make sure you are in the ml_env conda env.

import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Make tensor and normalize... Also you can add transforms if you like here later
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # probably should tune this to some optimal 
])

def get_data_loaders(batch_size=64):
    data_dir = './data'  # Ensure the correct path is specified here
    print("Loading data...")
    train_data = datasets.MNIST(root=data_dir, train=True, download=False, transform=transform)
    test_data = datasets.MNIST(root=data_dir, train=False, download=False, transform=transform)
    print("Data loaded.")
    train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False)
 
    return train_loader, test_loader

if __name__ == "__main__":
    batch_size = 8  # You can adjust the batch size
    train_loader, test_loader = get_data_loaders(batch_size)
    print(f"Train loader and test loader ready with batch size {batch_size}.")
