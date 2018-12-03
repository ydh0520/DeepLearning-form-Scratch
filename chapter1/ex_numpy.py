import numpy as np

x=np.array([1.0,2.0,3.0])
y=np.array([2.0,4.0,6.0])

# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x/2.0)

A=np.array([[1,2],[3,4]])

# print(A)
# print(A.shape)
# print(A.dtype)

B=np.array([[3,0],[0,6]])

# print(A+B)
# print(A*B)

#브로드 캐스트
# 형상이 다른 배열의 연산의 경우 확장되어 연산이 실행됨

#case1) 스칼라 -> 배열
# print(A*10)

#case2) 배열 -> 배열
B=np.array([10,20])
# print(A*B)


#원소의 접근
X=np.array([[51,55],[14,19],[0,4]])
# print(X)
# print(X[0])
# print(X[0][1])

#for row in X:
    # print(row)

#1차원 배열로 변환(평탄화)
X=X.flatten()
print(X)
#배열을 사용해 특정원소 추출
print(X[np.array([0,2,4])])
#조건을 통한 특정원소 추출
print(X>15)
print(X[X>15])