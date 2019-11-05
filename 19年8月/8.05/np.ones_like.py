import numpy as np
X = np.arange(1,13).reshape(3,4)
print(X)

X1 = np.ones_like(X)
print(X1)
X2 = np.zeros_like(X)
print(X2)