import os
from ultralytics import YOLO

HomeDirectory = os.getcwd()

modelDir = f"{HomeDirectory}/yolo-weights/yolov8n.pt"
dataDir = f"{HomeDirectory}/model/data.yaml"

print(HomeDirectory)
model = YOLO(modelDir)
results = model.train(data=dataDir, epochs=2000, batch_size=16, imgsz=640)
