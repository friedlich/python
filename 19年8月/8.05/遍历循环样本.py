import numpy as np
X = np.arange(1,13).reshape(3,4)
print(X)
print(X[:,3]) # 很明显，这个:有去括号的作用
print(X[:,0]) # 感觉没毛病呀

Y = np.array([0,1,0,1]).reshape(1,4)
print(Y)
print(Y[:,3])
print(Y[:,0])

permutation = list(np.random.permutation(3))
print(permutation)