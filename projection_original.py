from typing import Sequence, Text
import numpy as np
import math
from numpy.core.fromnumeric import shape
from numpy.core.numeric import flatnonzero
import pygame as pg
from pygame.event import event_name
from pygame.time import delay
from pygame.font import Font
from pygame import gfxdraw
from shapes import *
import random 
import os

from numpy.lib.function_base import angle, append
import time


def info(array):
    print(array)
    print("size: "+str(array.size))
    print("shape: "+str(array.shape))
    print("dtype: "+str(array.dtype))
res=800
fov=1

cube=np.loadtxt("/Users/danielshaked/bangkok/python_env/Lab/cubepoints.txt",float,delimiter=",")
#arrayx=np.loadtxt("box.txt",float,delimiter=",")
sphere=MakeSphere(1000)

modes="cube"
drawMode="line"
def xRotation(Angle,matrix):
    xAxisRotationMatrix=np.array(([1,0,0,0],[0,np.cos(Angle),-np.sin(Angle),0],[0,np.sin(Angle),np.cos(Angle),0],[0,0,0,1]))
    matrix=matrix@xAxisRotationMatrix
    return matrix
def yRotation(Angle,matrix):
    yAxisRotationMatrix=np.array(([np.cos(Angle),0,np.sin(Angle),0],[0,1,0,0],[-np.sin(Angle),0,np.cos(Angle),0],[0,0,0,1]))
    matrix=matrix@yAxisRotationMatrix
    return matrix
def zRotation(Angle,matrix):
    zAxisRotationMatrix=np.array(([np.cos(Angle),-np.sin(Angle),0,0],[np.sin(Angle),np.cos(Angle),0,0],[0,0,1,0],[0,0,0,1]))
    matrix=matrix@zAxisRotationMatrix
    return matrix
def OrthographicProjection(matrix,size):
    z0=(res*res/2)/(np.tan(90/2))
    arr=np.array(([z0,0,0,0],[0,z0,0,0],[0,0,1,0],[0,0,z0,0]),dtype=int)
    matrix=matrix@arr
    for x in range(matrix.shape[0]):
        matrix[x][2]=1/matrix[x][2]
    result=np.zeros(shape=(matrix.shape[0],2))
    for x in range(result.shape[0]):
        result[x][0]=matrix[x][0]*matrix[x][2]
        result[x][1]=matrix[x][1]*matrix[x][2]
    result=result*size
    return result
def PerspectiveProjection(matrix,size,fov):
    z0=1/(math.tan((fov/2)*math.pi/180))

    arr=np.array(([z0,0,0,0],[0,z0,0,0],[0,0,-1,0],[0,0,z0,0]),dtype=int)
    matrix=matrix@arr
    for x in range(matrix.shape[0]):
        matrix[x][2]=1/matrix[x][2]
    result=np.zeros(shape=(matrix.shape[0],2),dtype=np.float64)
    for x in range(result.shape[0]):
        result[x][0]=matrix[x][0]*matrix[x][2]
        result[x][1]=matrix[x][1]*matrix[x][2]
    result=result*size
    
    return result




    


    
    
    
def SwitchDrawModes(drawMode):
    if(drawMode=="line"):
        drawMode="pixel"
        return drawMode
    if(drawMode=="pixel"):
        drawMode="circle"
        return drawMode
    drawMode="line"
    return drawMode
    





fovMultiy=1
xAngle=0
yAngle=0
zAngle=0
pg.init()
#screen=pg.display.set_mode((0,0), pg.FULLSCREEN)
screen=pg.display.set_caption("3D to 2D Projection")
screen=pg.display.set_mode((res,res))



pg.display.update()
open=True
if(modes=="cube"):
 matrix=cube
if(modes=="sphere"):
 matrix=sphere
size=1

perspective=False
projectionState="Ortographic Projection"
font = pg.font.Font(pg.font.get_default_font(), 13)
frames=0
while(open):
    
    event = pg.event.poll()
    if event.type==pg.QUIT:
     open=False

    keys=pg.key.get_pressed()
    if keys[pg.K_UP]:
        xAngle=xAngle-0.0001
    if keys[pg.K_DOWN]:
        xAngle=xAngle+0.0001
    if keys[pg.K_RIGHT]:
        yAngle=yAngle-0.0001
    if keys[pg.K_LEFT]:
        yAngle=yAngle+0.0001
    if keys[pg.K_z]:
        zAngle=zAngle+0.0001
    if keys[pg.K_x]:
        zAngle=zAngle-0.0001
    if keys[pg.K_SPACE]:
        zAngle=0
        xAngle=0
        yAngle=0

    if keys[pg.K_s]:
        np.savetxt("saved_2D_matrix.txt",result,delimiter=",")
    if keys[pg.K_p]:
        perspective=True
        projectionState="Perspective Projection"
    if keys[pg.K_o]:
        perspective=False
        projectionState="Orthographic Projection"
    if keys[pg.K_u]:
        np.savetxt("saved_3D_matrix.txt",matrix,delimiter=",")
    if keys[pg.K_EQUALS]:
        size*=1.1
    if keys[pg.K_MINUS]:
        size*=0.9
    if keys[pg.K_d]:
        fov-=0.1
    if keys[pg.K_f]:
        fov+=0.1

    if keys[pg.K_r]:
        if(modes=="sphere"): matrix=sphere 
        else: matrix=cube
    if keys[pg.K_m]:
        delay(200)
        
        if(modes=="cube"):
            modes="sphere"
            matrix=sphere
        else:
            modes="cube"
            matrix=cube
    if keys[pg.K_n]:
        delay(200)
        drawMode=SwitchDrawModes(drawMode)
        print(drawMode)


    pg.display.update()
    matrix=xRotation(xAngle,matrix)
    matrix=yRotation(yAngle,matrix)
    matrix=zRotation(zAngle,matrix)
    frames=frames+1


    if(perspective):

        result=PerspectiveProjection(matrix,size,fov)
    else:

        result=OrthographicProjection(matrix,size)
    
    

    screen.fill("black")
    #text_surface, rect = font.render("Hello World!",True, (0, 0, 0))
    text_surface1 = font.render(projectionState+", "+"Field of view "+str(format(fov,".3f"))+", size "+str(size)+", Resolution "+str(res)+"X"+str(res), True, (255,250,80))
    text_surface2 = font.render("X Angle: "+str(format(xAngle,".3f"))+", Y Angle: "+str(format(yAngle,".3f"))+", Z Angle: "+str(format(zAngle,".3f"))+" Z0: "+str(format(1/(math.tan((fov/2)*math.pi/180)),".3f")), True, (255,250,80))

    screen.blit(text_surface1, (5,res-25))
    screen.blit(text_surface2, (5,(res-50)))
    
       

    for x in range(np.int64((result.shape[0]-1)/2)):
    #pg.draw.line(screen,(255,250,80),(result[x][0]+res/2,result[x][1]+res/2),(result[x+1][0]+res/2,result[x+1][1]+res/2),width=1)
        if(drawMode=="line"):
            gfxdraw.line(screen,np.int64(result[x][0]+res/2),np.int64(result[x][1]+res/2),np.int64(result[x+1][0]+res/2),np.int64(result[x+1][1]+res/2),(100,170,240))
        if(drawMode=="pixel"):
            gfxdraw.pixel(screen,np.int64(result[x][0]+res/2),np.int64(result[x][1]+res/2),(100,170,240))
        if(drawMode=="circle"):
            gfxdraw.circle(screen,np.int64(result[x][0]+res/2),np.int64(result[x][1]+res/2),10,(100,170,240))

    for x in range(np.int64((result.shape[0]-1)/2),(result.shape[0]-1)):
    #pg.draw.line(screen,(255,250,80),(result[x][0]+res/2,result[x][1]+res/2),(result[x+1][0]+res/2,result[x+1][1]+res/2),width=1)
        if(drawMode=="line"):
            gfxdraw.line(screen,np.int64(result[x][0]+res/2),np.int64(result[x][1]+res/2),np.int64(result[x+1][0]+res/2),np.int64(result[x+1][1]+res/2),(100,170,240))
        if(drawMode=="pixel"):
            gfxdraw.pixel(screen,np.int64(result[x][0]+res/2),np.int64(result[x][1]+res/2),(100,170,240))
        if(drawMode=="circle"):
            gfxdraw.circle(screen,np.int64(result[x][0]+res/2),np.int64(result[x][1]+res/2),10,(100,170,240))

                    
    #gfxdraw.aatrigon(screen,0,res,int(res/2),int(res/2),res,res,(255,255,255))

    pg.display.update()
   
pg.quit()
quit()
