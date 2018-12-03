import numpy as np
import matplotlib.pyplot as plt

#0~6까지 0.1간격으로 생성
x=np.arange(0,6,0.1)
y1=np.sin(x)

#그래프 그리기
# plt.plot(x,y1)
# plt.show()

#부가기능
y2=np.cos(x)

#그래프 그리기
plt.plot(x,y1,label="sin")
plt.plot(x,y2,linestyle="--",label="cos")#점선으로 그리기 
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin&cos")
plt.legend()#도표설명
plt.show()