import numpy as np


print("We create a 4x5 ndarray that contains integers from 0 to 19")
X = np.arange(20).reshape(4, 5)


print()
print("X = \n", X)
print()


Z = X[1:4, 2:5]

print()
print("Z = \n", Z)
print()


Z[2, 2] = 555


print()
print("X = \n", X)
print()
