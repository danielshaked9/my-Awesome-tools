import numpy as np
import mpl_toolkits.mplot3d
import matplotlib.pyplot as pp
from numpy.core.fromnumeric import reshape
from numpy.lib.function_base import append
import math

from numpy.lib.npyio import savetxt
def MakeSphere(num_pts):
    indices = np.arange(0, num_pts, dtype=float) + 0.5

    phi = np.arccos(1 - 2*indices/num_pts)
    theta = np.pi * (1 + 5**0.5) * indices

    x, y, z = np.cos(theta) * np.sin(phi), np.sin(theta) * np.sin(phi), np.cos(phi)
    w=np.ones((num_pts))
   # x=np.sort(x, axis=-1, kind="megasort", order=None)
  #  y=np.sort(y, axis=-1, kind=None, order=None)
   # z=np.sort(z, axis=-1, kind=None, order=None)
    array=np.column_stack((x,y,z,w))
    return array
def MinusPlusZero(x,y,z):
    minus=np.eye(3,3,-1)
    plus=np.eye(3,3,1)
    zero=np.eye(3,3,0)
    print("minus")
    print(minus)
    print("plus")
    print(plus)
    print("zero")
    print(zero)
def MakeRectangle(xSize,ySize,zSize,bothp=False,bothn=False):
    if(zSize==None):
        pointA=[-(xSize/2),-(ySize/2)]
        pointB=[(xSize/2),(-ySize/2)]
        pointC=[xSize/2,ySize/2]
        pointD=[xSize/2,-(ySize/2)]
        square=[pointA,pointB,pointC,pointD]
        return square
    if(zSize!=None):
        pointA=[-(xSize/2),-(ySize/2),zSize/2,1]
        pointB=[(xSize/2),(-ySize/2),zSize/2,1]
        pointC=[xSize/2,ySize/2,zSize/2,1]
        pointD=[xSize/2,-(ySize/2),zSize/2,1]
        square=[pointA,pointB,pointC,pointD]
        return square
    


def MakeBox(xSize,ySize,zSize):
    square1=MakeRectangle(xSize,ySize,zSize)
    square2=MakeRectangle(xSize,ySize,-zSize)
    square3=MakeRectangle(-xSize,ySize,-zSize)
    square4=MakeRectangle(-xSize,-ySize,-zSize)
    square5=MakeRectangle(xSize,-ySize,-zSize)
    square6=MakeRectangle(xSize,-ySize,-zSize)
    square7=MakeRectangle(xSize,-ySize,zSize)
    square8=MakeRectangle(xSize,-ySize,zSize)


    
    
    return square1+square2+square3+square4+square5+square6+square7+square8

    
    


box=MakeBox(5,5,5)
box=np.array(box)
np.savetxt("box.txt",box,delimiter=",")





