# Importing all necessary libraries
import cv2 as cv
import os

# Read the video from specified path
cam = cv.VideoCapture(r"C:\Users\danie\Documents\rune-detection\newdata\runes.mp4")

try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')

# frame
currentframe = 0

while(True):
    
    # reading from frame
    ret,frame = cam.read()
    currentframe += 1
    if ret and currentframe % 60 == 0:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.png'
        print ('Creating...' + name)

        # writing the extracted images
        cv.imwrite(name, frame)
        

        # increasing counter so that it will
        # show how many frames are created
        
    else:
        if currentframe > 10000:
            break

# Release all space and windows once done
cam.release()
cv.destroyAllWindows()