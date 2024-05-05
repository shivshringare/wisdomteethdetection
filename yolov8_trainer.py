from ultralytics import YOLO

# Initialize YOLOv8 model
model = YOLO('yolov8n')

# Train the model
model.train(mode='train', data='data.yaml', epochs=100, device='gpu', batch=64, workers=4, val=False, name='training_results', cache=True)
