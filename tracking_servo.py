import numpy as np
import cv2 as cv
import math
import time
import serial

arduinoData = serial.Serial('com3', 9600)
totalFrame = 0
frameTime = 15

cropped = None
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# xy of click
def draw(event, x, y, flag, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(f"x: {x} y: {y} ")


cv.namedWindow('frame')
cv.setMouseCallback('frame', draw)
while True:
    totalFrame += 1
    ret, frame = cap.read()
    height, width = frame.shape[:2]
    mask = np.zeros(frame.shape[:2], dtype="uint8")
    cv.rectangle(mask, (0, 0), (width, height//2), 255, -1)
    maskedFrame = cv.bitwise_and(frame, frame, mask=mask)
    
    # image clean up
    gray = cv.cvtColor(maskedFrame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    thresh = cv.adaptiveThreshold(
    blur, 255,
    cv.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv.THRESH_BINARY_INV,
    11, 2
    )
    
    # fix noise in center of frame
    cv.rectangle(thresh, (width//2 - 20, height//2 - 5), (width//2 + 20, height//2 + 5), 0, -1)
    
    # contour
    contours, hierarchies = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    min_area = 1500  # how big contour
    filtered_contours = [c for c in contours if cv.contourArea(c) > min_area]
    
    # draw biggest contour
    if filtered_contours:
        largest_contour = max(filtered_contours, key=cv.contourArea)
        cv.drawContours(frame, [largest_contour], -1, (0, 255, 0), 2)

    for contour in filtered_contours:
        # centroid and angle
        M = cv.moments(contour)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            # center to get angle
            x, y = width//2, height//2

            dx = cx - x
            dy = cy - y

            cv.line(frame, (cx, cy), (x,y), (0,0,255), 3)

            angle_rad = math.atan2(dy, dx)
            angle_deg = math.degrees(angle_rad)
            if(angle_deg <= 0):
                angle_deg += 180
            
            # send to arduino (adjust frameTime to increase/decrease output)
            if totalFrame >= frameTime:
                cmd = round(angle_deg, 2)

                print(cmd)
                strCmd = str(cmd) + '\r'
                arduinoData.write(strCmd.encode())
                frameTime += 15
                print(f" total frame:{totalFrame}")
                print(f" frametime:{frameTime}")
            
        bx, by, bw, bh = cv.boundingRect(contour)
        # cropped = frame[by:by+bh, bx:bx+bw]
  
    if cropped is not None:
        cv.imshow("Cropper", cropped)
        cropped_RGB = cv.cvtColor(cropped, cv.COLOR_BGR2RGB)
    
    cv.imshow("frame", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv.destroyAllWindows()