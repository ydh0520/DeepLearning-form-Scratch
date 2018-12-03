def AND(x1,x2):
    w1,w2,theta=0.5,0.5,0.7
    tmp=x1*w1+x2*w2
    if tmp<=theta:
        return 0
    elif tmp>theta:
        return 1

def testAND():
    print("--- AND ---")
    print(AND(0,0))
    print(AND(1,0))
    print(AND(0,1))
    print(AND(1,1))

#testAND()

#가중치와 편향의 도입 
# theta 를 -b로 치환하며 출력의 기준을 0으로 설정
import numpy as np

x=np.array([0,1]) #입력
w=np.array([0.5,0.5]) #가중치
b=-0.7 #편향
# print(x*w)
# print(np.sum(x*w))
# print(np.sum(x*w)+b)

#가중치와 편향을 도입한 and
def fixAND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.7
    tmp=np.sum(x*w)+b
    if tmp<=0:
        return 0
    else:
        return 1

def testfixAND():
    print("--- FIXED AND ---")
    print(fixAND(0,0))
    print(fixAND(1,0))
    print(fixAND(0,1))
    print(fixAND(1,1))

#testfixAND()

def NAND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([-0.5,-0.5])
    b=0.7
    tmp=np.sum(x*w)+b
    if tmp<=0:
        return 0
    else:
        return 1

def OR(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.2
    tmp=np.sum(x*w)+b
    if tmp<=0:
        return 0
    else:
        return 1

def testNAND():
    print("--- NAND ---")
    print(NAND(0,0))
    print(NAND(1,0))
    print(NAND(0,1))
    print(NAND(1,1))

def testOR():
    print("--- OR ---")
    print(OR(0,0))
    print(OR(1,0))
    print(OR(0,1))
    print(OR(1,1))

# testNAND()
# testOR()

#퍼셉트론의 한계
# 1.xor을 표현할수 없다.
# 2.곡선을 표현할수 없다.

#회로의 조합을 통하여 xor을 표현 
def XOR(x1,x2):
    s1=NAND(x1,x2)
    s2=OR(x1,x2)
    y=fixAND(s1,s2)
    return y

def testXOR():
    print("--- XOR ---")
    print(XOR(0,0))
    print(XOR(1,0))
    print(XOR(0,1))
    print(XOR(1,1))

testXOR()