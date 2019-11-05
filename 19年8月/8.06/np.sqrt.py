import numpy as np
np.random.seed(3)
L = [2, 4, 1]
parameters = {}
for l in range(1, len(L)):
    print(L[l-1])
    print(np.sqrt(2 / L[l - 1]))
    parameters['W' + str(l)] = np.random.randn(L[l], L[l - 1]) * np.sqrt(2 / L[l - 1])
    parameters['b' + str(l)] = np.zeros((L[l], 1))
print(parameters)
print(0.5**0.5)
print(0.7071067811865476**2)