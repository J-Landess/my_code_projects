import torch
import torch.nn as nn

class LeNet(nn.Module):
    def __init__(self):
        super(LeNet, self).__init__()
        
        # LeNet architecture: 2 convolutional layers followed by fully connected layers
        self.conv1 = nn.Conv2d(1, 6, kernel_size=5, stride=1, padding=0)  # Input: 1x28x28, Output: 6x24x24
        self.pool = nn.AvgPool2d(kernel_size=2, stride=2, padding=0)      # Pooling
        self.conv2 = nn.Conv2d(6, 16, kernel_size=5, stride=1, padding=0) # Output: 16x8x8
        self.fc1 = nn.Linear(16 * 4 * 4, 120)  # Fully connected layer
        self.fc2 = nn.Linear(120, 84)          # Fully connected layer
        self.fc3 = nn.Linear(84, 10)           # Output layer (10 classes for MNIST)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))  # Apply conv1, ReLU, and pooling
        x = self.pool(torch.relu(self.conv2(x)))  # Apply conv2, ReLU, and pooling
        x = x.view(-1, 16 * 4 * 4)  # Flatten the output for fully connected layers
        x = torch.relu(self.fc1(x))  # Apply first fully connected layer with ReLU
        x = torch.relu(self.fc2(x))  # Apply second fully connected layer with ReLU
        x = self.fc3(x)  # Apply final fully connected layer (output layer)
        return x
