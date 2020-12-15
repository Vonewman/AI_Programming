import numpy as np
import matplotlib.pyplot as plt


np.random.seed(1)
n = 50
x = np.random.randn(n)
y = x * np.random.randn(n)


colors = np.random.randn(n)
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))


plt.scatter(x, y, c=colors, alpha=0.5)
plt.show()


x_values = [i for i in range(11)]
print(x_values)


# Convert to numpy
x_train = np.array(x_values, dtype=np.float32)
print(x_train.shape)


# IMPORTANT: 2D required
x_train = x_train.reshape(-1, 1)
print(x_train.shape)
y_values = [2*i + 1 for i in x_values]
print(y_values)


y_train = np.array(y_values, dtype=np.float32)
print(y_train.shape)


# IMPORTANT: 2D required
y_train = y_train.reshape(-1, 1)
print(y_train.shape)
