
from cv2 import cubeRoot
from matplotlib.pyplot import axis
import numpy as np
import cv2 as cv
from Projection_Engine_V2 import *
def cam_change_x(val):
    cam_pt[0]=val
def cam_change_y(val):
    cam_pt[1]=val
def cam_change_z(val):
    cam_pt[2]=val
def cam_or_change_x(val):
    cam_or[0]=val
def cam_or_change_y(val):
    cam_or[1]=val
def cam_or_change_z(val):
    cam_or[2]=val
def Cube_Points_Gen(counter=40,cube=[0,0,0],mat=np.empty((40,3))):
    if counter==0:
        return mat
    mat[40-counter]=cube
    a,ac,b,bc,c,cc=cube[0], not cube[0], cube[1], not cube[1], cube[2], not cube[2]
    Cube_Points_Gen(counter=counter-1, cube=[b and c or a and b, ac and c or ac and b or b and c, ac or bc and c], mat=mat)
    return mat
    
    
    
resx=512
resy=512
cam_pt=[100,100,1000]
cam_or=[-1,1,-1]
disp_sur=[300,300,3000]
matrix1=np.loadtxt("cubepoints1.txt",float,delimiter=",")*100
matrix2=np.loadtxt("cubepoints2.txt",float,delimiter=",")*100
# Create a black image
img = np.zeros((resx,resy,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
i=1
windowName="Display Window"
while(True):
    #e1 = cv.getTickCount()
    # your code execution
    cv.imshow("Display Window", img)
    #xAxisS=yRotation(0.0001,xAxisS)
    #yAxisS=yRotation(0.0001,yAxisS)
    #zAxisS=yRotation(0.0001,zAxisS)
    #cam_or=zRotation(0.001,cam_or)
    #cam_pt[0]=cam_pt[0]*0.1
    #cam_pt[0]=cam_pt[0]+1
    #cam_pt=zRotation(0.001,cam_pt)
    #print(cam_pt)
    #xAxis=PerspectiveProjectionMatrix(xAxisS,cam_pt,cam_or,disp_sur,True)
   # yAxis=PerspectiveProjectionMatrix(yAxisS,cam_pt,cam_or,disp_sur,True)
    #zAxis=PerspectiveProjectionMatrix(zAxisS,cam_pt,cam_or,disp_sur,True)
    cube1=PerspectiveProjectionMatrix(matrix1,cam_pt,cam_or,disp_sur,True)
    cube2=PerspectiveProjectionMatrix(matrix2,cam_pt,cam_or,disp_sur,True)
    matrix1=xRotation(0.001,matrix1)
    matrix1=yRotation(0.001,matrix1)
    #matrix1=zRotation(0.011,matrix1)
    matrix2=xRotation(0.001,matrix2)
    matrix2=yRotation(0.001,matrix2)
    #matrix2=zRotation(0.011,matrix2)
    img = np.zeros((512*2, 512*2, 3), dtype=np.uint8)
    #cv.polylines(img,np.int32([xAxis]),0,(255,0,0),thickness=3) # x BLUE
    #cv.polylines(img,np.int32([yAxis]),0,(0,255,0),thickness=3) # y GREEN
    #cv.polylines(img,np.int32([zAxis]),0,(0,0,255),thickness=3) # z RED
    cv.polylines(img,np.int32([cube2]),1,(100,100,100),thickness=3) # z RED
    cv.polylines(img,np.int32([cube1]),1,(100,100,100),thickness=3) # z RED
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()

