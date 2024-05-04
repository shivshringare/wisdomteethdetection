from ultralytics import YOLO

TRAINED_MODEL_PATH = 'trained_model'

# Initialize YOLOv8 model
model = YOLO('yolov8n') # mps for Apple M1/M2 chips

# Train the model
model.train(mode='train', data='data.yaml', device='mps')
