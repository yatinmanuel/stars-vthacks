import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Error: Could not open camera.')
    exit()

cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, image = cap.read()
    cv2.imshow('Cam', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
