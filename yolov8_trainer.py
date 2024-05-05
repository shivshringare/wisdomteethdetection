from ultralytics import YOLO

# Initialize YOLOv8 model
model = YOLO('yolov8n')

# Train the model
model.train(mode='train', data='data.yaml', device='mps', val=False, name='training_results', cache=True)
