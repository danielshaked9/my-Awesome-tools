import numpy as np
import cv2 as cv
from projection_V2 import *
import os
import screeninfo


def clearConsole():
    command = 'clear'
    os.system(command)

fov=45
matrix=np.loadtxt("/Users/danielshaked/bangkok/python_env/Lab/saved_3D_matrix.txt",float,delimiter=",")
cube=matrix
cube=cube+200
cube=PerspectiveProjection(matrix,300,fov)

# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
cube=np.array(cube,dtype=np.int32)
cube = cube.reshape((-1,1,2))
while(True):
    #e1 = cv.getTickCount()
    # your code execution
    cv.polylines(img,[cube],True,(0,255,255))
    cv.imshow("Display Window", img)
    matrix=xRotation(0.004,matrix)
    matrix=yRotation(0.008,matrix)
    matrix=zRotation(0.0019,matrix)
    cube=PerspectiveProjection(matrix,100,fov)
    cube=np.array(cube,dtype=np.int32)
    cube=cube+200
    cube = cube.reshape((-1,1,2))
    img = np.zeros((512, 512, 3), dtype=np.float32)
    #e2 = cv.getTickCount()
    #time = (e2 - e1)/ cv.getTickFrequency()
    #print(time)
    #clearConsole()
    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()