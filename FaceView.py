import cv2
import numpy as np
import serial

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# ser = serial.Serial('/dev/ttyACM0')
servRange = 180
xInc = 0
yInc = 0

cv2.namedWindow("FaceTracker")
cv2.createTrackbar("x", "FaceTracker", 20, 200, lambda doNothing: None)
cv2.createTrackbar("y", "FaceTracker", 20, 200, lambda doNothing: None)

while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(image=gray, scaleFactor=1.15, minNeighbors=5)

    for (x, y, w, h) in faces:
        data = "X{0:.0f}Y{1:.0f}"
        center = (x + w/2, y + h/2)
        xPrecision = cv2.getTrackbarPos("x", "FaceTracker")
        yPrecision = cv2.getTrackbarPos("y", "FaceTracker")

        if(center[0] > width/2 + xPrecision):
            xInc = -1
        elif(center[0] < width/2 - xPrecision):
            xInc = 1
        else:
            xInc = 0
        if(center[1] > height/2 + yPrecision):
            yInc = 1
        elif(center[1] < height/2 - yPrecision):
            yInc = -1
        else:
            yInc = 0
        
        data = data.format(xInc, yInc)
        print(data + "   " + str(center[0]) + ":" + str(width/2)
            + "   " + str(center[1]) + ":" + str(height/2))
        # ser.write(data.encode())
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)

        cv2.imshow("FaceTracker", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break