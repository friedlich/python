import numpy as np

Z = np.array([[1.2,-1.5,-1.8]])
print(Z)
print(Z.shape)
A = np.maximum(0,Z)
print(A)
assert(A.shape == Z.shape)
print(A) #我觉得已经print的很清楚了

