import numpy as np
X = np.arange(25).reshape(5, 5)


print()
print("Original X = \n", X)
print()


print("The elements in X that are greater than 10:", X[X > 10])
print("The elements in X that less than or equal to 7:", X[X <= 7])
print("The elements in X that are between 10 and 17:", \
      X[(X > 10) & (X < 17)])


print("We use Boolean indexing to assign the elements that are \
between 10 and 17 the value of -1")
X[(X > 10) & (X < 17)] = -1


print()
print('X = \n', X)
print()
