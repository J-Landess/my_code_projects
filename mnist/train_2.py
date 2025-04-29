import cv2
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
    
    print("Loading data...")
    train_loader, test_loader = get_data_loaders(batch_size=8)
    print("Data loaded.")

    model = LeNet().to(device)
    model_path = "/Users/justinlandess/my_code_projects/mnist/saved_models/model_epoch_50.pth"

    if os.path.exists(model_path):
        model.load_state_dict(torch.load(model_path, map_location=device))
        print(f"✅ Loaded model from {model_path}")
    else:
        print(f"⚠️ Model file not found at {model_path}. Training from scratch.")

    criterion = nn.CrossEntropyLoss() 
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    epochs = 1
    model_dir = "saved_models"
    os.makedirs(model_dir, exist_ok=True)

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

            _, preds = torch.max(outputs, 1)

            labels_np = labels.cpu().numpy()
            preds_np = preds.cpu().numpy()

            acc = accuracy_score(labels_np, preds_np)
            prec = precision_score(labels_np, preds_np, average='weighted', zero_division=0)
            rec = recall_score(labels_np, preds_np, average='weighted', zero_division=0)
            f1 = f1_score(labels_np, preds_np, average='weighted', zero_division=0)

            batch_accuracies.append(acc)
            batch_precisions.append(prec)
            batch_recalls.append(rec)
            batch_f1_scores.append(f1)

        print(f"✅ Epoch {epoch+1} completed.")
        evaluate_model(test_loader, model, device)

    plot_metrics(batch_losses, batch_accuracies)

def evaluate_model(test_loader, model, device):    
    model.eval()
    all_preds, all_labels = [], []
    
    shown = 0
    max_shown = 5  # Show only 5 incorrect predictions

    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, preds = torch.max(outputs, 1)

            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())

            for img, pred, label in zip(images, preds, labels):
                if pred != label and shown < max_shown:
                    img_np = img.cpu().numpy().squeeze() * 255
                    img_np = img_np.astype(np.uint8)
                    img_np = cv2.resize(img_np, (200, 200), interpolation=cv2.INTER_NEAREST)
                    cv2.putText(img_np, f"Pred: {pred.item()}, True: {label.item()}", 
                                (10, 190), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255, 1)
                    cv2.imshow("Incorrect Prediction", img_np)
                    print(f"Showing incorrect prediction — Pred: {pred.item()}, True: {label.item()}")
                    key = cv2.waitKey(0) & 0xFF
                    if key == ord('q'):
                        break
                    shown += 1
        cv2.destroyAllWindows()

    accuracy = accuracy_score(all_labels, all_preds)
    precision = precision_score(all_labels, all_preds, average='weighted')
    recall = recall_score(all_labels, all_preds, average='weighted')
    f1 = f1_score(all_labels, all_preds, average='weighted')
    
    print(f"\n📊 Evaluation Results:")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print(f"Precision: {precision:.4f} | Recall: {recall:.4f} | F1: {f1:.4f}")

def plot_metrics(losses, accuracies):
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(losses, label="Batch Loss", color='red')
    plt.xlabel("Batch")
    plt.ylabel("Loss")
    plt.title("Training Loss Per Batch")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(accuracies, label="Batch Accuracy", color='blue')
    plt.xlabel("Batch")
    plt.ylabel("Accuracy")
    plt.title("Training Accuracy Per Batch")
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    train_model()
