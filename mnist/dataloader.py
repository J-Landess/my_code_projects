import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Define the transformation: convert to tensor and normalize
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # Normalize the images
])

# # Define a function to get the data loaders
# def get_data_loaders(batch_size=64):
#     print("Loading data...")
#     train_data = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
#     test_data = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
#     print("Data loaded.")
    
#     train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
#     test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False)
    
#     return train_loader, test_loader


def get_data_loaders(batch_size=64):
    data_dir = './data'  # Ensure the correct path is specified here
    print("Loading data...")
    train_data = datasets.MNIST(root=data_dir, train=True, download=False, transform=transform)
    test_data = datasets.MNIST(root=data_dir, train=False, download=False, transform=transform)
    print("Data loaded.")
    train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False)
    
    return train_loader, test_loader
