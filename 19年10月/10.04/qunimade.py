import numpy as np

Y = np.arange(1,25).reshape(4,6)
print(Y)
m = Y.shape[0]
permutation = list(np.random.permutation(m))
print(permutation)
shuffled_Y = Y[permutation,:]
print(shuffled_Y)
shuffled_Y = Y[:,permutation]
print(shuffled_Y)
# 原来一切的一切都是方向的问题