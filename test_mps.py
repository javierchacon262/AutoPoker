from ultralytics import YOLO
import torch

# Check if MPS is available
device = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Using device: {device}")

# Load the YOLO model
model = YOLO("yolov8n.pt")  # Using the nano model (smallest & fastest)

# Train YOLOv8 on custom poker cards dataset
model.train(data="poker_cards.yaml", epochs=50, device=device)
