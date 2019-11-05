import numpy as np 
print(np.sqrt(5))
print(5/np.sqrt(5))

L = [5,4,3]
np.random.seed(1)
parameters = {}
for l in range(1, len(L)):
    print(L[l])
    print(L[l - 1]) 
    print(np.sqrt(L[l-1]))
    parameters['W' + str(l)] = np.random.randn(L[l], L[l - 1]) 
    print(parameters['W' + str(l)])
    print(parameters['W' + str(l)] / np.sqrt(L[l-1]))
    # TypeError：/：'NoneType'和'float'不支持的操作数类型

