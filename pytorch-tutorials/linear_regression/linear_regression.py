import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import pandas as pd

sns.set_style(style='whitegrid')
plt.rcParams["patch.force_edgecolor"] = True


# Create a single training set with the available data set as shown below
m = 2
c = 3
x = np.random.rand(256)


noise = np.random.randn(256) / 4


y = x * m + c + noise


df = pd.DataFrame()
df['x'] = x
df['y'] = y


sns.lmplot(x='x', y='y', data=df)


import torch
import torch.nn as nn
from torch.autograd import variable


x_train = x.reshape(-1, 1).astype('float32')
y_train = y.reshape(-1, 1).astype('float32')


class LinearRegressionModel(nn.Model):
    def __init__(self, input_dim, output_dim):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def foward(self, x):
        out = self.linear(x)
        return out


input_dim = x_train.shape[1]
output_dim = y_train.shape[1]
input_dim, output_dim(1, 1)
model = LinearRegressionModel(input_dim, output_dim)
criterion = nn.MSELoss()
[w, b] = model.parameters()


import torch
import torch.nn as nn
from torch.autograd import Variable
x_train = x.reshape(-1, 1).astype('float32')
y_train = x.reshape(-1, 1).astype('float32')


class LinearRegressionModel(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        out = self.linear(x)
        return out


input_dim = x_train.shape[1]
output_dim = y_train.shape[1]

print(input_dim)
