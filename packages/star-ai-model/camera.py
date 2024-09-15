# Libary imports
from ultralytics import YOLO
import math
import cv2

# Start the camera and set the resolution
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Error: Could not open camera.')
    exit()

cap.set(3, 640)
cap.set(4, 480)

# Load the YOLO model
model = YOLO('yolo-weights/yolov8n.pt')

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush", "eyeballs", "eyebrows", "eyes", "face", "facial hair"
              ]
# AI Logic
while True:
    ret, image = cap.read()

    results = model(image, stream=True)
    for r in results:
        boxes = r.boxes

        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            confidence = math.ceil((box.conf[0] * 100)) / 100
            print(confidence)

            cls = int(box.cls)
            print(classNames[cls])

            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (0, 255, 0)
            thickness = 2
            cv2.putText(image, classNames[cls], org, font, fontScale, color, thickness)
    cv2.imshow('Camera', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
