from random import random
from matplotlib.lines import Line2D
import numpy as np
from numpy.core.fromnumeric import mean
import pandas as pd
from matplotlib import pyplot as plt
np.random.seed(1001)
X=np.arange(0,100)
Y=np.arange(0,100)
#X=X+np.random.rand(1,100)
#X=np.random.uniform(0,100,[1,100]) # A 1x100 array
#X=X+np.random.uniform(0,0,[1,500]) # A 1x100 array
Y=Y+np.random.uniform(-70,200,[1,100]) # A 1x100 array

# Building the model
b = 1
bias = mean(Y)
#bias=0

L = 0.0001  # The learning Rate
epochs = 10000  # The number of iterations to perform gradient descent

n = float(len(X)) # Number of elements in X
r_squared=[]
beta=[]
pred=[]
# Performing Gradient Descent 
for i in range(epochs): 
    Y_pred = b*X + bias  # The current predicted value of Y
    b_error = (-2/n) * sum(X * (Y - Y_pred))  # Derivative wrt m
    D_c = (-2/n) * sum(Y - Y_pred)  # Derivative wrt c
    b = b - L * b_error  # Update beta

    bias = bias - L * D_c  # Update bias
    print("epoch: "+str(i))
full=np.array([X,Y,Y_pred])
print(full.shape)
df=pd.DataFrame(columns=['x','y','pred'])
print(df)
plt.scatter(X, Y) 
#plt.scatter(X,Y_pred,color='red')
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')  # regression line
plt.show()