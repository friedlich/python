import numpy as np
dA = np.array([[1, 2],
               [3, 4],
               [5, 6]])
print(dA)
Z = np.array([[-2.77991749, -2.82513147],
       [-0.11407702, -0.01812665],
       [ 2.13860272,  1.40818979]])
dZ = np.array(dA, copy=True)
print(dZ)
dZ[Z <= 0] = 0
print(dZ)