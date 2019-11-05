# 在numpy模块中，我们经常会使用resize 和 reshape,在具体使用中，通常是使用resize改变数组的尺寸大小，
# 使用reshape用来增加数组的维度。

# 给数组一个新的形状而不改变其数据
import numpy as np
X=np.array([1,2,3,4,5,6,7,8])
    
X_2=X.reshape((2,4)) #return a 2*4 2-dim array
X_3=X.reshape((2,2,2)) # return a 2*2*2 3-dim array
    
print("X:\n",X)
print("X_2:\n",X_2)
print("X_3:\n",X_3)
