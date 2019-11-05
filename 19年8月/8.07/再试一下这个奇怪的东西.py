import numpy as np

C = 6
Y = np.eye(C)
print(Y)
print(np.eye(C)[[1,1,0,0,3,2,4,5]])  # 这句话有两个[][]，意思应该是定位到里面来给里面的1索引位置重新定位
print(np.eye(C)[[1,1,0,0,3,2,4,5]].T)
