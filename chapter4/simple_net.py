import sys,os
sys.path.append(os.getcwd())
import numpy as np
from common.function import softmax,cross_entropy_error
from common.gradient import numerical_gradient

class simpleNet:
    def __init__(self):
        self.W=np.random.randn(2,3)

    def predict(self,x):
        return np.dot(x,self.W)

    def loss(self,x,t):
        z=self.predict(x)
        y=softmax(z)
        loss=cross_entropy_error(y,t)

        return loss

def f(W):
    return net.loss(x,t)

net =simpleNet()
print(net.W)

x=np.array([0.6,0.9])
p=net.predict(x)

print(p)

np.argmax(p)

t=np.array([0,0,1])
net.loss(x,t)

dW=numerical_gradient(f,net.W)
print(dW)