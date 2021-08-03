import numpy as np
import matplotlib.pyplot as plt


n = 50

d = 1
x = np.random.uniform(-1, 1, (n, d))

weights_true = np.array([[5], ])
bias_true = np.array([10])


y_true = x @ weights_true + bias_true
print("x: {}, weights: {}, bias: {}, y: {}"
      .format(x.shape, weights_true.shape, bias_true.shape, y_true.shape))

plt.plot(x, y_true, marker='x', label='underlying function')
plt.legend()
plt.show()


class Linear:

    def __init__(self, num_input, num_output=1):
        self.weights = np.random.randn(num_input, num_output) * \
            np.sqrt(2. / num_input)
        self.bias = np.zeros((1))

    def __call__(self, x):
        return x @ self.weights + self.bias


linear = Linear(d)
y_pred = linear(x)
plt.plot(x, y_true, marker='x', label='underlying function')
plt.scatter(x, y_pred, color='r', marker='.', label='out function')
plt.legend()
plt.show()


# Basic loss function: MSE
class MSE:
    def __call__(self, y_pred, y_true):
        self.y_pred = y_pred
        self.y_true = y_true
        return ((y_true - y_pred) ** 2).mean()


loss = MSE()
print(f'Our initial loss is {loss(y_pred, y_true)}')
