import numpy as np

X = np.arange(1,97).reshape(2,4,4,3)
print(X)
X_flatten = X.reshape(X.shape[0],-1).T
print(X_flatten.shape)
# print(X_flatten)

X1 = X.reshape(-1)
print(X1)
print(X1.shape)
X2 = X.reshape(4,-1)
print(X2)
print(X2.shape)
X3 = X.reshape(4,3,-1)
print(X3)
print(X3.shape)

# 到此应该已经很明显了，reshape中-1就是本来的维度的乘积除去你前面自定义的的维度，前面的维度没有的话默认除1