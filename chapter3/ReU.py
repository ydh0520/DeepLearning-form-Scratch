import numpy as np
import matplotlib.pylab as plt

def ReLU(x):
    return np.maximum(0,x)

def drow_ReLU():
    x=np.arange(-5.0,5.0,0.1)
    y=ReLU(x)
    plt.plot(x,y)
    plt.ylim(-0.1,1.1)
    plt.show()

drow_ReLU()
