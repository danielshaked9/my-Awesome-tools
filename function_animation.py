import itertools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

def f():
    arr=np.linspace(0,100,10000)
    for i in range(10000):
        x = arr[i]
        if x==0:
            yield x, 0.00001
        else:
            yield x, np.sin(x)


def init():
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,
fig, ax = plt.subplots()
ax.set_ylim(-1.1,1.1)
ax.set_xlim(0,5)
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []



def run(data):
    # update the data
    x, y = data
    xdata.append(x)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    if x >= xmax:
        ax.set_xlim(xmin,np.e*xmax )
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)


ani = animation.FuncAnimation(fig, run, f(), interval=1, init_func=init)
plt.show()

