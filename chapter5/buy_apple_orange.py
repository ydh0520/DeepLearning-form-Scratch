import sys,os
sys.path.append(os.getcwd())
from AddLayer import AddLayer
from MulLayer import MulLayer

apple = 100
orange = 150
apple_num=2
orange_num=3
tax=1.1

mul_apple_layer=MulLayer()
mul_orange_layer=MulLayer()
mul_tax_layer=MulLayer()
add_apple_orange_layer=AddLayer()

apple_price=mul_apple_layer.forward(apple,apple_num)
orange_price=mul_orange_layer.forward(orange,orange_num)
total_price=add_apple_orange_layer.forward(apple_price,orange_price)
price=mul_tax_layer.forward(total_price,tax)

print(price)

dprice=1
dtotal_price,dtax=mul_tax_layer.backward(dprice)
print(dtotal_price,dtax)
dapple_price,dorange_price=add_apple_orange_layer.backward(dtotal_price)
print(dapple_price,dorange_price)
dapple,dapple_num=mul_apple_layer.backward(dapple_price)
print(dapple,dapple_num)
dorange,dorange_num=mul_orange_layer.backward(dorange_price)
print(dorange,dorange_num)