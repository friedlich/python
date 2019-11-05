import numpy as np
e = np.arange(216).reshape(6,3,3,4)
print(e)
print(e.shape)
print(e.reshape(e.shape[0],-1))
print((e.reshape(e.shape[0],-1)).shape)
print(e.reshape(e.shape[0],-1).T)
print((e.reshape(e.shape[0],-1).T).shape)