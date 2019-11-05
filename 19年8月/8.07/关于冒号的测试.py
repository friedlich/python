import numpy as np
Y = np.arange(1, 7).reshape(1, 6)
print(Y)
print(Y[0, 2])
print(Y[:, 2])
print(np.squeeze(Y[:, 2]))