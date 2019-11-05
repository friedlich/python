import numpy as np 
X = np.arange(1,49).reshape(4,12)
print(X)
np.random.seed(10)
permutation = list(np.random.permutation(12))
print(permutation)
shuffled_X = X[:, permutation]
print(shuffled_X)

print()
np.random.seed(11)
permutation = list(np.random.permutation(12))
print(permutation)
shuffled_X = X[:, permutation]
print(shuffled_X)

print()
np.random.seed(12)
permutation = list(np.random.permutation(12))
print(permutation)
shuffled_X = X[:, permutation]
print(shuffled_X)

print()
np.random.seed(13)
permutation = list(np.random.permutation(12))
print(permutation)
shuffled_X = X[:, permutation]
print(shuffled_X)

print()
np.random.seed(14)
permutation = list(np.random.permutation(12))
print(permutation)
shuffled_X = X[:, permutation]
print(shuffled_X)

print()
np.random.seed(10)
permutation = list(np.random.permutation(12))
print(permutation)
shuffled_X = X[:, permutation]
print(shuffled_X)

