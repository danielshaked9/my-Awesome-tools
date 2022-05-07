from ast import arg
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
#cube=np.loadtxt("/Users/danielshaked/bangkok/python_env/Lab/cubepoints.txt",float,delimiter=",")
points=500
def xRotation(Angle,matrix):
    xAxisRotationMatrix=np.array((1,0,0,0,np.cos(Angle),-np.sin(Angle),0,np.sin(Angle),np.cos(Angle))).reshape(3,3)
    matrix=matrix@xAxisRotationMatrix
    return matrix
def yRotation(Angle,matrix):
    yAxisRotationMatrix=np.array((np.cos(Angle),0,np.sin(Angle),0,1,0,-np.sin(Angle),0,np.cos(Angle))).reshape(3,3)
    matrix=matrix@yAxisRotationMatrix
    return matrix
def zRotation(Angle,matrix):
    zAxisRotationMatrix=np.array((np.cos(Angle),-np.sin(Angle),0,np.sin(Angle),np.cos(Angle),0,0,0,1)).reshape(3,3)
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
def PerspectiveProjectionPoint(a_xyz, c_xyz, theta, e_xyz,negative): 
    """(projected point ,camera point,orientation of camera, display surface)"""
    a=np.array(a_xyz)
    c=np.array(c_xyz)
    first=np.array((1, 0, 0 , 0, np.cos(theta[0]), np.sin(theta[0]), 0, -np.sin(theta[0]), np.cos(theta[0]))).reshape(3,3)
    second=np.array((np.cos(theta[1]), 0, -np.sin(theta[1]), 0, 1, 0, np.sin(theta[1]), 0, np.cos(theta[1]))).reshape(3,3)
    third=np.array((np.cos(theta[2]), np.sin(theta[2]), 0, -np.sin(theta[2]), np.cos(theta[2]), 0, 0, 0, 1)).reshape(3,3)
    fourth=np.array((a-c))
    d_xyz=np.array(((first*second*third*fourth)@np.ones((3,1))))
    if e_xyz[2]==0:
        f_xyz=np.array((1, 0, e_xyz[0]/0.0001, 0, 1, e_xyz[1]/0.0001, 0, 0, 1/0.0001)).reshape(3,3)@d_xyz
    else:
        f_xyz=np.array((1, 0, e_xyz[0]/e_xyz[2], 0, 1, e_xyz[1]/e_xyz[2], 0, 0, 1/e_xyz[2])).reshape(3,3)@d_xyz
    if f_xyz[2]==0:
        bx=f_xyz[0]/0.00001
        by=f_xyz[1]/0.00001
    else:
        bx=f_xyz[0]/f_xyz[2]
        by=f_xyz[1]/f_xyz[2]
    if not negative:
        if by<0: by=-by
        if bx<0: bx=-bx
        
    return (bx,by)
def PerspectiveProjectionMatrix(point_mat,camera_point,camera_orientation,display_surface,negative=False):
    projected=np.empty((point_mat.shape[0],point_mat.shape[1]-1))
    for i in range(point_mat.shape[0]):
        projected[i][:]=PerspectiveProjectionPoint(point_mat[i],camera_point,camera_orientation,display_surface,negative)
    return projected
