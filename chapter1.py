import cv2

print("Package Imported")

## Lectura de imagenes
'''
img = cv2.imread("")
cv2.imshow("Output",img)
cv2.waitKey(0) # Infinite delay
'''
## Load video
'''
cap = cv2.VideoCapture("")

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''

## Capture the webcam

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
