# import torch
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
