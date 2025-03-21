import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from collections import Counter

# Make tensor and normalize... Also you can add transforms if you like here later
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # probably should tune this to some optimal
])

def count_class_distribution(data_loader):
    # Initialize a counter to count class occurrences
    class_counter = Counter()
    
    # Iterate through the data loader
    for _, labels in data_loader:
        # Move labels to CPU (if they're on GPU) and convert to numpy
        labels = labels.cpu().numpy()  
        class_counter.update(labels)
    
    return class_counter

def get_data_loaders(batch_size=64):
    data_dir = './data'  # Ensure the correct path is specified here
    print("Loading data...")
    train_data = datasets.MNIST(root=data_dir, train=True, download=False, transform=transform)
    test_data = datasets.MNIST(root=data_dir, train=False, download=False, transform=transform)
    print("Data loaded.")
    train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False)
 
    return train_loader, test_loader

def run(batch_size=64):
    # Get data loaders
    train_loader, test_loader = get_data_loaders(batch_size)
    print(f"Train loader and test loader ready with batch size {batch_size}.")
    
    # Count class distribution in the training data
    train_class_distribution = count_class_distribution(train_loader)
    print("Training set class distribution:", train_class_distribution)

    # Count class distribution in the test data
    test_class_distribution = count_class_distribution(test_loader)
    print("Test set class distribution:", test_class_distribution)

# Only run this part if this script is executed as the main script
if __name__ == "__main__":
    run(batch_size=8)

# import torch
# from torchvision import datasets, transforms
# from torch.utils.data import DataLoader
# from collections import Counter

# # Make tensor and normalize... Also you can add transforms if you like here later
# transform = transforms.Compose([
#     transforms.ToTensor(),
#     transforms.Normalize((0.5,), (0.5,))  # probably should tune this to some optimal
# ])

# def count_class_distribution(data_loader):
#     # Initialize a counter to count class occurrences
#     class_counter = Counter()
    
#     # Iterate through the data loader
#     for _, labels in data_loader:
#         # Move labels to CPU (if they're on GPU) and convert to numpy
#         labels = labels.cpu().numpy()  
#         class_counter.update(labels)
    
#     return class_counter

# def get_data_loaders(batch_size=64):
#     data_dir = './data'  # Ensure the correct path is specified here
#     print("Loading data...")
#     train_data = datasets.MNIST(root=data_dir, train=True, download=False, transform=transform)
#     test_data = datasets.MNIST(root=data_dir, train=False, download=False, transform=transform)
#     print("Data loaded.")
#     train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
#     test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False)
 
#     return train_loader, test_loader

# if __name__ == "__main__":
#     batch_size = 8  # You can adjust the batch size
#     train_loader, test_loader = get_data_loaders(batch_size)
#     print(f"Train loader and test loader ready with batch size {batch_size}.")
    
#     # Count class distribution in the training data
#     train_class_distribution = count_class_distribution(train_loader)
#     print("Training set class distribution:", train_class_distribution)

#     # Count class distribution in the test data
#     test_class_distribution = count_class_distribution(test_loader)
#     print("Test set class distribution:", test_class_distribution)

# import torch
# from torchvision import datasets, transforms
# from torch.utils.data import DataLoader
# from collections import Counter

# # Make tensor and normalize... Also you can add transforms if you like here later
# transform = transforms.Compose([
#     transforms.ToTensor(),
#     transforms.Normalize((0.5,), (0.5,))  # probably should tune this to some optimal 
# ])
# def count_class_distribution(data_loader):
#     # Initialize a counter to count class occurrences
#     class_counter = Counter()
    
#     # Iterate through the data loader
#     for _, labels in data_loader:
#         class_counter.update(labels.numpy())
    
#     return class_counter
# def get_data_loaders(batch_size=64):
#     data_dir = './data'  # Ensure the correct path is specified here
#     print("Loading data...")
#     train_data = datasets.MNIST(root=data_dir, train=True, download=False, transform=transform)
#     test_data = datasets.MNIST(root=data_dir, train=False, download=False, transform=transform)
#     print("Data loaded.")
#     train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
#     test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False)
 
#     return train_loader, test_loader

# if __name__ == "__main__":
#     batch_size = 8  # You can adjust the batch size
#     train_loader, test_loader = get_data_loaders(batch_size)
#     print(f"Train loader and test loader ready with batch size {batch_size}.")
#     train_class_distribution = count_class_distribution(train_loader)
#     print("Training set class distribution:", train_class_distribution)

#     # Count class distribution in the test data
#     test_class_distribution = count_class_distribution(test_loader)
#     print("Test set class distribution:", test_class_distribution)
import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, WeightedRandomSampler
import numpy as np

# Define transformation
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # You can adjust this if needed
])

def get_data_loaders(batch_size=64, imbalance_factor=1.0):
    data_dir = './data'  # Ensure the correct path is specified here
    print("Loading data...")
    
    # Load MNIST dataset
    train_data = datasets.MNIST(root=data_dir, train=True, download=False, transform=transform)
    test_data = datasets.MNIST(root=data_dir, train=False, download=False, transform=transform)
    
    print("Data loaded.")
    
    # Compute class weights (inverse frequency)
    class_counts = np.zeros(10)  # There are 10 classes (0 to 9)
    for label in train_data.targets:
        class_counts[label] += 1
    
    # Calculate the weights for each class (inverse of frequency)
    class_weights = 1. / class_counts
    sample_weights = class_weights[train_data.targets]  # Assign weight to each sample

    # Adjusting for imbalance (multiply by the imbalance_factor to exaggerate the effect)
    sample_weights = sample_weights * imbalance_factor
    
    # Create WeightedRandomSampler to apply class balancing
    sampler = WeightedRandomSampler(weights=sample_weights, num_samples=len(sample_weights), replacement=True)
    
    # Create DataLoader with sampler
    train_loader = DataLoader(train_data, batch_size=batch_size, sampler=sampler)
    test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False)  # No imbalance in test data
    
    return train_loader, test_loader

if __name__ == "__main__":
    batch_size = 8  
    imbalance_factor = 8.0  # Factor by which to increase imbalance. 1.0 is balanced, >1 increases imbalance
    train_loader, test_loader = get_data_loaders(batch_size, imbalance_factor)
    print(f"Train loader and test loader ready with batch size {batch_size} and imbalance factor {imbalance_factor}.")
