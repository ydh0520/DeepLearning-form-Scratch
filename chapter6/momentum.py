import numpy as np
#물체의 속도를 의미하는 v 변수를 계산에 추가하여 갱신할때 기울기에 따라 갱신하는 값의 크기에 가중치를 부여한다.
class Momentum:
    def __init__(self,lr=0.01,momentum=0.9):
        self.lr=lr
        self.momentum=momentum
        self.v=None
        
    def update(self,params,grads):
        if self.v is None:
            self.v={}
            for key,val in params.items():
                self.v[key] = np.zeros_like(val)
        
        for key in params.keys():
            self.v[key] = self.momentum*self.v[key]-self.lr*grads[key]
            params[key]+=self.v[key]

