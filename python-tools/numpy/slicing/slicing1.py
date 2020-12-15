import numpy as np


print("We create a 4 x 5 ndarray that contains integers from 0 to 19")
X = np.arange(20).reshape(4, 5)


# We print X
print()
print('X = \n', X)
print()

print("We select all the elements that are in the 2nd row through 4th rows \
and in the 3rd to 5th columns")
W = X[1:, 2:5]


print()
print("W = \n", W)


print("We select all the elements that are in 1st through create a 4 x 5 \
ndarray that contains integers from 0 to 19")
Y = X[:3, 2:5]


print()
print("Y = \n", Y)
print()


print("We select all the elements in the 3rd row")
v = X[2, :]


print()
print("v = ", v)


print("We select all the elements in the 3rd column")
q = X[:, 2]


print()
print('q = ', q)


print("We select all the elements in the 3rd column but return \
a rank 2 ndarray")
R = X[:, 2:3]


print()
print("R = \n", R)
