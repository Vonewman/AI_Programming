import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torch.autograd import Variable

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
print('\n')
# convert to numpy
x_train = np.shape(x_values, dtype=np.float32)
print(x_train.shape)


print("Reshape x_train to be a 2D array:\n")
x_train = x_train.reshape(-1, 1)
print(x_train.shape)


y_values = [2*i + 1 for i in x_values]
print(y_values)
print('\n')
# convert to numpy
y_train = np.array(y_values, dtype=np.float32)
print(y_train.shape)


class LinearRegressionModel(nn.Module):
    def __init__(self, input_size, output_size):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        out = self.linear(x)
        return out


input_dim = 1
output_dim = 1

model = LinearRegressionModel(input_dim, output_dim)


criterion = nn.MSELoss()


learning_rate = 0.01
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

epochs = 100

for epoch in range(epochs):
    epoch += 1
    # convert numpy array to torch Variable
    inputs = Variable(torch.from_numpy(x_train))
    labels = Variable(torch.from_numpy(y_train))

    # clear gradients w.r.t parameters
    optimizer.zero_grad()

    # Forward to get out
    outputs = model(inputs)

    # Calculate Loss
    loss = criterion(outputs, labels)

    # getting gradients w.r.t parameters
    loss.backward()

    # Updating parameters
    optimizer.step()

    print('epoch {}, loss {}'.format(epoch, loss.item()))


# Purely inference
predicted = model(Variable(torch.from_numpy(x_train))).data.numpy()
predicted


# y = 2x + 1
print(y_train)


# Clear figure
plt.clf()

# Get predictions
predicted = model(Variable(torch.from_numpy(x_train))).data.numpy()

# Plot true data
plt.plot(x_train, y_train, 'go', label='True data', alpha=0.5)

# Plot predictions
plt.plot(x_train, predicted, '--', label='Predictions', alpha=0.5)

# Legend and plot
plt.legend(loc='best')
plt.show()
