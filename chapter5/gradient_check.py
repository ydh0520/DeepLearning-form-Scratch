#오차역전파법은 빠른 계산이 가능하나 구현의 복잡함 때문에 오류 발생 가능성이 높다.
#따라서 비교적 구현이 쉽고 오류발생 가능성이 적은 수치비문을 통하여 오차역전파법의 계산을 검증한다.
import sys,os
sys.path.append(os.getcwd())
import numpy as np
from common.dataset import load_mnist
from TwoLayerNet import TwoLayerNet

(x_train,t_train),(x_test,t_test)=load_mnist(normalize=True,one_hot_label=True)

network=TwoLayerNet(input_size=784,hidden_size=50,output_size=10)

x_batch=x_train[:3]
t_batch=t_train[:3]

grad_numerical=network.numerical_gradient(x_batch,t_batch)
grad_backprop=network.gradient(x_batch,t_batch)

for key in grad_numerical.keys():
    diff=np.average(np.abs(grad_backprop[key]-grad_numerical[key]))
    print(key+":"+str(diff))

