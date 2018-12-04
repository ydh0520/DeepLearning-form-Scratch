import numpy as np
import matplotlib.pylab as plt

def step_function_scalar(x):
    if x>0:
        return 1
    else :
        return 0

def setp_function(x):
    #다음 조건식을 사용하여 x의 인자들을 boolean으로 변경
    y=x>0
    #astype자료형 변환 함수
    return y.astype(np.int)
    #다음과 같이 한줄로도 변경 가능
    #return y.astype(x>0,np.int)

def drow_step_function():
    x=np.arange(-5.0,5.0,0.1)
    y=setp_function(x)
    plt.plot(x,y)
    plt.ylim(-0.1,1.1)
    plt.show()

drow_step_function()