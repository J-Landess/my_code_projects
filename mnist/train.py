import torch
import torch.nn as nn
import torch.optim as optim
from dataloader import get_data_loaders
from model import LeNet

# Training function
def train_model():
    # Check if CUDA is available, otherwise use CPU
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    # Get data loaders
    train_loader, test_loader = get_data_loaders(batch_size=8)
    
    # Initialize the LeNet model and move it to the device
    model = LeNet().to(device)
    
    # Loss function and optimizer
    criterion = nn.CrossEntropyLoss()  # CrossEntropyLoss works for multi-class classification
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    # Training loop
    epochs = 25
    for epoch in range(epochs):
        model.train()  # Set the model to training mode
        running_loss = 0.0
        
        for images, labels in train_loader:
            # Move images and labels to the device
            images, labels = images.to(device), labels.to(device)
            
            optimizer.zero_grad()  # Zero the gradients
            
            # Forward pass
            outputs = model(images)
            
            # Compute the loss
            loss = criterion(outputs, labels)
            
            # Backward pass and optimize
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item()
        
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {running_loss/len(train_loader):.4f}")
        
        # Evaluate the model after every epoch
        evaluate_model(test_loader, model, device)
    
    print("Training Finished!")

# Function to evaluate the model on the test dataset
def evaluate_model(test_loader, model, device):
    model.eval()  # Set the model to evaluation mode
    correct = 0
    total = 0
    with torch.no_grad():  # Disable gradient calculation during evaluation
        for images, labels in test_loader:
            # Move images and labels to the device
            images, labels = images.to(device), labels.to(device)
            
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    
    accuracy = 100 * correct / total
    print(f"Test Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    train_model()
    