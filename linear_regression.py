from random import random
from matplotlib.lines import Line2D
import numpy as np
from numpy.core.fromnumeric import mean, size
import pandas as pd
from matplotlib import pyplot as plt
from loading_bar import *
from tqdm import tqdm
import time
np.random.seed(1001)
X=np.arange(0,70)
Y=np.arange(0,70)
#X=X+np.random.rand(1,100)
#X=np.random.uniform(0,100,[1,100]) # A 1x100 array
#X=X+np.random.uniform(0,0,[1,500]) # A 1x100 array
Y=Y+np.random.uniform(-755000,288000,[1,70]) # A 1x100 array

# Building the model
b = 1
bias = mean(Y)
#bias=0

L = 0.001  # The learning Rate
epochs = 100  # The number of iterations to perform gradient descent

n = float(len(X)) # Number of elements in X
r_squared=[]
beta=[]
pred=[]
num_of_bars=0
# Performing Gradient Descent 
for i in tqdm(range(epochs)):
    Y_pred = b*X + bias  # The current predicted value of Y
    b_error = (-2/n) * sum(X * (Y - Y_pred))  # Derivative wrt m
    D_c = (-2/n) * sum(Y - Y_pred)  # Derivative wrt c
    b = b - L * b_error  # Update beta

    bias = bias - L * D_c  # Update bias
    #print("epoch: "+str(i),end='\r')
    
full=np.array([X,Y,Y_pred],dtype=object)
df=pd.DataFrame(columns=['x','y','pred'])
plt.scatter(X, Y,marker='.') 
#plt.scatter(X,Y_pred,color='red')
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')  # regression line
plt.show()

