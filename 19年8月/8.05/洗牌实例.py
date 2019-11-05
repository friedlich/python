import numpy as np
X = np.arange(1,13).reshape(3,4)
Y = np.array([0,1,0,1]).reshape(1,4)
print(X)
print(Y)
permutation = list(np.random.permutation(4))
print(permutation)
shuffled_X = X[:, permutation]
print(shuffled_X)
shuffled_X = X[permutation, :]  # index 3 is out of bounds for axis 0 with size 3
print(shuffled_X)
shuffled_Y = Y[:, permutation]
# shuffled_Y = Y[:, permutation].reshape((1,4))
print(shuffled_Y)
print(shuffled_X[:,0:2])
print(shuffled_Y[:,0:2])
print(shuffled_X[:,2:])
print(shuffled_Y[:,2:])