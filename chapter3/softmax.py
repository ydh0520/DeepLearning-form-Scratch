#입력에 대하여 출력값의 합이 1이 되게 변환시켜주는 함수

import numpy as np

def softmax(a):
    exp_a=np.exp(a)
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a

    return y

a=np.array([0.3,2.9,4.0])
print(softmax(a))

#다음과 같은 방식은 오버플로로 인하여 에러발생 가능성이 높다
#따라서 각 입력값에 임의의 값을 대입하여 올바른 값을 유도한다.
#일반적으로 임의의 값은 배열의 가장 작은 값으로 한다.
def fix_softmax(a):
    c=np.max(a)
    exp_a=np.exp(a-c)
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a

    return y

def compare():
    a=np.array([1010,1000,990])
    print("--- 개선 전 ---")
    print(softmax(a))
    print("--- 개선 후 ---")
    print(fix_softmax(a))

compare()