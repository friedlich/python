# 在numpy模块中，我们经常会使用resize 和 reshape,在具体使用中，通常是使用resize改变数组的尺寸大小，
# 使用reshape用来增加数组的维度。

# 1.resize
# 之前看到别人的博客说，resize没有返回值，其实这取决于你如何使用resize,resize有两种使用方式，一种是没有返回值的，
# 直接对原始的数据进行修改，还有一种用法是有返回值的，所以不会修改原有的数组值。

# 1.1有返回值，不对原始数据进行修改
import numpy as np
X=np.array([[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]])
    
X_new=np.resize(X,(3,3)) # do not change the original X
print("X:\n",X)  #original X
print("X_new:\n",X_new) # new X

# 1.2 无返回值，直接修改原始数组的大小
print()
import numpy as np
X=np.array([[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]])
    
X_2=X.resize((3,3))  #change the original X ,and do not return a value
print("X:\n",X)  # change the original X
print("X_2:\n",X_2) # return None


