import numpy as np
A1 = np.arange(1,7).reshape(2,3)
D1 = np.random.rand(A1.shape[0], A1.shape[1])     
print(D1)
D1 = D1 < 0.86
print(D1)   