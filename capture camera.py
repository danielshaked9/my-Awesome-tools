import numpy as np
import cv2 as cv
# importing the modules
import qrcode

# enter the data for qr code
Data="Daniel"

# create a filename
filename="Qrcode.jpg"

# generate the qrcode
qr=qrcode.make(Data)

# save the image
# the image will be saved in
# the same directory
# you can also give a path
qr.save(filename)
qr = cv.imread('Qrcode.jpg',0)
w, h = qr.shape[::-1]
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Apply template Matching
    res = cv.matchTemplate(gray,qr,0)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(gray,top_left, bottom_right, 255, 2)

    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()