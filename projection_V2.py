import numpy as np
import math
def info(array):
    print(array)
    print("size: "+str(array.size))
    print("shape: "+str(array.shape))
    print("dtype: "+str(array.dtype))
resx=1650
resy=1050
fov=30
cube=np.loadtxt("/Users/danielshaked/bangkok/python_env/Lab/cubepoints.txt",float,delimiter=",")
points=500
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
def forward(matrix):
    forwardarr=np.zeros_like(matrix)
    forwardarr[:,1]=0.01
    matrix=matrix-forwardarr
    return matrix
def backward(matrix):
    backwardarr=np.zeros_like(matrix)
    backwardarr[:,1]=0.01
    matrix=matrix+backwardarr
    return matrix
def leftward(matrix):
    leftwardarr=np.zeros_like(matrix)
    leftwardarr[:,0]=0.01
    matrix=matrix-leftwardarr
    return matrix
def rightward(matrix):
    rightwardarr=np.zeros_like(matrix)
    rightwardarr[:,0]=0.01
    matrix=matrix+rightwardarr
    return matrix
def zforward(matrix):
    leftwardarr=np.zeros_like(matrix)
    leftwardarr[:,2]=0.01
    matrix=matrix-leftwardarr
    return matrix
def zbackward(matrix):
    rightwardarr=np.zeros_like(matrix)
    rightwardarr[:,2]=0.01
    matrix=matrix+rightwardarr
    return matrix
def OrthographicProjection(matrix,size):
    z0=(resx/2)/(np.tan(90/2))
    arr=np.array(([z0,0,0,0],[0,z0,0,0],[0,0,1,0],[0,0,z0,0]),dtype=int)
    matrix=matrix@arr
    matrix[:,2]=1/matrix[:,2]
    result=np.zeros(shape=(matrix.shape[0],2),dtype=np.float64)
    result[:,0]=matrix[:,0]*matrix[:,2]
    result[:,1]=matrix[:,1]*matrix[:,2]
    result=result*size
    return result
def PerspectiveProjection(matrix,size,fov):
    z0=1/(math.tan((fov/2)*math.pi/180))
    arr=np.array(([z0,0,0,0],[0,z0,0,0],[0,0,-1,0],[0,0,z0,0]),dtype=int)
    matrix=matrix@arr
    matrix[:,2]=1/matrix[:,2]
    result=np.zeros(shape=(matrix.shape[0],2),dtype=np.float64)
    result[:,0]=matrix[:,0]*matrix[:,2]
    result[:,1]=matrix[:,1]*matrix[:,2]
    return result*size
