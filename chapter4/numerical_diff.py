import numpy as np
import matplotlib.pylab as plt

#수치 미분
def numerical_diff(f,x):
    h=1e-4 #반올림 오차 문제로 인하여 10e-50에서 변경
    return (f(x+h)-f(x-h))/(2*h) #중앙차분을 통하여 오차 개선

def function_1(x):
    return 0.01*x**2+0.1*x

def test_function_1():
    x=np.arange(0.0,20.1,0.1)
    y=function_1(x)


    print(numerical_diff(function_1,5))
    print(numerical_diff(function_1,10))

    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x,y)
    plt.show()

def function_2(x):    
    if x.ndim == 1:
        return np.sum(x**2)
    else:
        return np.sum(x**2, axis=1)

def compare_diff():
    #각각 x0과 x1을 기준으로 하여 편미분을 구하고 비교해 본다.
    x0,x1=3,4
    def function_temp1(x0):
        return x0*x0+4.0**2
    
    def function_temp2(x1):
        return x1*x1+3.0**2
    
    print(numerical_diff(function_temp1,x0))
    print(numerical_diff(function_temp2,x1))

def numerical_gradient(f,x):
    #주어진 함수의 편미분을 동시에 계산
    h=1e-4
    grad=np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]
        
        x[idx]=tmp_val+h
        fxh1=f(x)

        x[idx]=tmp_val-h
        fxh2=f(x)

        grad[idx]=(fxh1-fxh2)/(2*h)
        x[idx]=tmp_val

    return grad

def test_numerical_gradient():
    print(numerical_gradient(function_2,np.array([3.0,4.0])))
    print(numerical_gradient(function_2,np.array([0.0,2.0])))
    print(numerical_gradient(function_2,np.array([3.0,0.0])))


def _numerical_gradient_no_batch(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x) # x와 형상이 같은 배열을 생성
    
    for idx in range(x.size):
        tmp_val = x[idx]
        
        # f(x+h) 계산
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)
        
        # f(x-h) 계산
        x[idx] = tmp_val - h 
        fxh2 = f(x) 
        
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val # 값 복원
        
    return grad


def numerical_gradient_ex(f, X):
    if X.ndim == 1:
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)
        
        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_no_batch(f, x)
        
        return grad

def show_numerical_gradient():
    x0 = np.arange(-2, 2.5, 0.25)
    x1 = np.arange(-2, 2.5, 0.25)
    X, Y = np.meshgrid(x0, x1)

    X = X.flatten()
    Y = Y.flatten()

    grad = numerical_gradient_ex(function_2, np.array([X, Y]) )

    plt.figure()
    plt.quiver(X, Y, -grad[0], -grad[1],  angles="xy",color="#666666")#,headwidth=10,scale=40,color="#444444")
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.xlabel('x0')
    plt.ylabel('x1')
    plt.grid()
    plt.legend()
    plt.draw()
    plt.show()