import numpy as np


class MSE:

    def __call__(self, y_pred, y_true):
        self.y_pred = y_pred
        self.y_true = y_true
        return ((y_pred - y_true) ** 2).mean()

    def backward(self):
        n = self.y_train.shape[0]
        self.gradient = 2. * (self.y_pred - self.y_true) / n
        return self.gradient


class Linear:

    def __init__(self, input_dim: int, num_hidden: int = 1):
        self.weights = np.random.randn(input_dim, num_hidden) - 0.5
        self.bias = np.random.randn(1) - 0.5

    def __call__(self, x):
        self.x = x
        output = x @ self.weights + self.bias
        return output

    def backward(self, gradient):
        self.weights_gradient = self.x.T @ gradient
        self.bias_gradient = gradient @ self.weights.T
        self.x_gradient = gradient @ self.weights
        return self.x_gradient

    def update(self, lr):
        self.weights = self.weights - lr * self.bias_gradient
        self.bias = self.bias - lr * self.bias_gradient

n = 50
d = 1
x = np.random.uniform(-1, 1, (n, d))
loss = MSE()
Linear = Linear()
y_pred = linear(x)
print(loss(y_pred, y_true))
