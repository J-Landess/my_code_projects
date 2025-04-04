import os
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from dataloader import get_data_loaders
from model import LeNet

def train_model():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    train_loader, test_loader = get_data_loaders(batch_size=8)
    
    model = LeNet().to(device)
    criterion = nn.CrossEntropyLoss() 
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    epochs = 5
    batch_losses = []
    batch_accuracies = []
    model_dir = "saved_models"
    os.makedirs(model_dir,exist_ok=True)
    # Initialize lists to store metrics per batch
    batch_losses = []
    batch_accuracies = []
    batch_precisions = []
    batch_recalls = []
    batch_f1_scores = []

    for epoch in range(epochs):
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            batch_losses.append(loss.item())

            # Convert outputs to predictions
            _, preds = torch.max(outputs, 1)

            # Convert tensors to NumPy arrays
            labels_np = labels.cpu().numpy()
            preds_np = preds.cpu().numpy()

            # Compute metrics
            acc = accuracy_score(labels_np, preds_np)
            prec = precision_score(labels_np, preds_np, average='weighted', zero_division=0)
            rec = recall_score(labels_np, preds_np, average='weighted', zero_division=0)
            f1 = f1_score(labels_np, preds_np, average='weighted', zero_division=0)

            # Store the metrics
            batch_accuracies.append(acc)
            batch_precisions.append(prec)
            batch_recalls.append(rec)
            batch_f1_scores.append(f1)

        print(f"Epoch {epoch+1} completed.")

    # Plot the metrics after training
    plot_metrics(batch_losses, batch_accuracies, batch_precisions, batch_recalls, batch_f1_scores)
    # for epoch in range(epochs):
    #     model.train()
    #     running_loss = 0.0
    #     batch_idx = 0
        
    #     for images, labels in train_loader:
    #         images, labels = images.to(device), labels.to(device)
    #         optimizer.zero_grad()
            
    #         outputs = model(images)
    #         loss = criterion(outputs, labels)
    #         loss.backward()
    #         optimizer.step()
            
    #         running_loss += loss.item()
    #         batch_losses.append(loss.item())

    #         # Compute batch accuracy
    #         _, preds = torch.max(outputs, 1)
    #         batch_accuracy = accuracy_score(labels.cpu().numpy(), preds.cpu().numpy())
    #         batch_accuracies.append(batch_accuracy)

    #         # Print batch metrics
    #         if batch_idx % 100 == 0:  # Print every 10 batches
    #             print(f"Epoch [{epoch+1}/{epochs}], Batch [{batch_idx}/{len(train_loader)}], "
    #                   f"Loss: {loss.item():.4f}, Accuracy: {batch_accuracy * 100:.2f}%")
            
    #         batch_idx += 1
        
    #     model_path = os.path.join(model_dir, f"model_epoch_{epoch+1}.pth")
    #     torch.save(model.state_dict(), model_path)
        
    #     print(f"Model saved at: {model_path}")
    #     print(f"Epoch [{epoch+1}/{epochs}], Avg Loss: {running_loss / len(train_loader):.4f}")
    #     evaluate_model(test_loader, model, device)

    # print("Training Finished!")

    # # Plot Loss and Accuracy
    # plot_metrics(batch_losses, batch_accuracies)

def evaluate_model(test_loader, model, device):    
    model.eval()
    all_preds, all_labels = [], []
    
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, preds = torch.max(outputs, 1)

            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
    
    all_preds, all_labels = np.array(all_preds), np.array(all_labels)
    accuracy = accuracy_score(all_labels, all_preds)
    precision = precision_score(all_labels, all_preds, average='weighted')
    recall = recall_score(all_labels, all_preds, average='weighted')
    f1 = f1_score(all_labels, all_preds, average='weighted')

    print(f"Test Accuracy: {accuracy * 100:.2f}% | Precision: {precision:.4f} | Recall: {recall:.4f} | F1: {f1:.4f}")

def plot_metrics(losses, accuracies):
    plt.figure(figsize=(12, 5))

    # Plot Loss
    plt.subplot(1, 2, 1)
    plt.plot(losses, label="Batch Loss", color='red')
    plt.xlabel("Batch")
    plt.ylabel("Loss")
    plt.title("Training Loss Per Batch")
    plt.legend()

    # Plot Accuracy
    plt.subplot(1, 2, 2)
    plt.plot(accuracies, label="Batch Accuracy", color='blue')
    plt.xlabel("Batch")
    plt.ylabel("Accuracy")
    plt.title("Training Accuracy Per Batch")
    plt.legend()

    plt.show()

if __name__ == "__main__":
    train_model()
