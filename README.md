# Wisdom Teeth Analysis using image enhancement techniques and YoloV8

Before you begin, ensure you have met the following requirements:
- Python 3.11 or later
- Pip package manager
- An environment manager like venv (optional, but recommended)

## Setup Python Virtual Environment
`python -m venv env`

## Activate the virtual environment
### On Windows:
`venv\Scripts\activate`
### On Linux or MacOS:
`source venv/bin/activate`

## Setup
### Install PyTorch
`pip install torch torchvision torchaudio`

### Install Ultralytics YOLOv8 package
`pip install ultralytics`

## Usage
- Run `yolov8_trainer.py` to train the model
- The trainer loads data from the datasets folder, this can be configured in `data.yaml` file by updating the `path` to `../wisdomteethdetection/datasets/<your-dataset>/`
  
