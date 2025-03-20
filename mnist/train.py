# import torch
# import torch.nn as nn
# import torch.optim as optim
# from dataloader import get_data_loaders
# from model import LeNet


# def train_model():
#     # Check if CUDA is available, otherwise use CPU
#     device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
#    # you can set the batch size here
#     train_loader, test_loader = get_data_loaders(batch_size=8)
    
    
#     model = LeNet().to(device)
    
#     # Loss and optimizer
#     criterion = nn.CrossEntropyLoss() 
#     optimizer = optim.Adam(model.parameters(), lr=0.001)# tried learning rate .003
    
#     # Training loop
#     epochs = 5
#     for epoch in range(epochs):
#         model.train()  # Set the model to training mode
#         running_loss = 0.0
        
#         for images, labels in train_loader:
#             # Move images and labels to the device
#             images, labels = images.to(device), labels.to(device)
            
#             optimizer.zero_grad()  # Zero the gradients
            
#             # Forward pass
#             outputs = model(images)
            
#             # Compute the loss
#             loss = criterion(outputs, labels)
            
#             # Backward pass and optimize
#             loss.backward()
#             optimizer.step()
            
#             running_loss += loss.item()
        
#         print(f"Epoch [{epoch+1}/{epochs}], Loss: {running_loss/len(train_loader):.4f}")
        
#         # Evaluate_model() after every epoch
#         evaluate_model(test_loader, model, device)
    
#     print("Training Finished!")

# # Function to evaluate the model on the test dataset
# def evaluate_model(test_loader, model, device):
#     model.eval()  # Set the model to evaluation mode
#     correct = 0
#     total = 0
#     with torch.no_grad():  # Disable gradient  during eval
#         for images, labels in test_loader:
#             # Move images and labels to the device
#             images, labels = images.to(device), labels.to(device)
            
#             outputs = model(images)
#             _, predicted = torch.max(outputs, 1)
#             total += labels.size(0)
#             correct += (predicted == labels).sum().item()
    
#     accuracy = 100 * correct / total
#     print(f"Test Accuracy: {accuracy:.2f}%")

# if __name__ == "__main__":
#     train_model()

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from dataloader import get_data_loaders
from model import LeNet
import numpy as np

def train_model():
    # Check if CUDA is available, otherwise use CPU
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    # Set the batch size here
    train_loader, test_loader = get_data_loaders(batch_size=8)
    
    # Initialize model, loss function, and optimizer
    model = LeNet().to(device)
    criterion = nn.CrossEntropyLoss() 
    optimizer = optim.Adam(model.parameters(), lr=0.001)  # You can tune the learning rate
    
    # Training loop
    epochs = 5
    for epoch in range(epochs):
        model.train()  # Set the model to training mode
        running_loss = 0.0
        
        # Training phase
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
        
        # Print training loss for the current epoch
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {running_loss/len(train_loader):.4f}")
        
        # Evaluate model performance after every epoch
        evaluate_model(test_loader, model, device)
    
    print("Training Finished!")

# Function to evaluate the model on the test dataset and print performance metrics
def evaluate_model(test_loader, model, device):
    model.eval()  # Set the model to evaluation mode
    
    all_preds = []
    all_labels = []
    
    with torch.no_grad():  # Disable gradient calculation during evaluation
        for images, labels in test_loader:
            # Move images and labels to the device
            images, labels = images.to(device), labels.to(device)
            
            # Forward pass
            outputs = model(images)
            
            # Get the predicted class
            _, preds = torch.max(outputs, 1)
            
            # Store predictions and true labels
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
    
    # Convert lists to numpy arrays
    all_preds = np.array(all_preds)
    all_labels = np.array(all_labels)
    
    # Compute performance metrics
    accuracy = accuracy_score(all_labels, all_preds)
    precision = precision_score(all_labels, all_preds, average='weighted')  # Weighted for multi-class
    recall = recall_score(all_labels, all_preds, average='weighted')      # Weighted for multi-class
    f1 = f1_score(all_labels, all_preds, average='weighted')              # Weighted for multi-class
    conf_matrix = confusion_matrix(all_labels, all_preds)
    
    # Print the results
    print(f"Test Accuracy: {accuracy * 100:.4f}%")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-Score: {f1:.4f}")
    print("\nConfusion Matrix:")
    print(conf_matrix)
    print("\nClassification Report:")
    print(classification_report(all_labels, all_preds))

if __name__ == "__main__":
    train_model()

    