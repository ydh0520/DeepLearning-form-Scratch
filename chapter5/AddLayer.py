class AddLayer:
    def __init__(slef):
        pass

    def forward(self,x,y):
        out=x+y
        return out

    def forward(self,dout):
        dx=dout*1
        dy=dout*1

        return dx,dy