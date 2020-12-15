import torch
import torch.nn as nn
import torch.nn.functional as F


class LogisticModel(nn.Module):
    def __init__(self, in_dim, out_dim):
        super(LogisticModel, self).__init__()
        self.linear = nn.Linear(in_dim, out_dim)

    def forward(self, x):
        out = F.sigmoid(self.linear(x))
        return out


in_dim, out_dim = 1, 1
model = LogisticModel(1, 1)


criterion = torch.nn.BCELoss(size_average=True)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)


x_train = torch.tensor([[1.6], [2.1], [1.3], [4.8], [3.5]],
                       dtype=torch.float).reshape(-1, 1)
y_train = torch.tensor([[0], [0], [0], [1], [1]],
                       dtype=torch.float).reshape(-1, 1)

epochs = 1000
for epoch in range(epochs):
    inputs, labels = x_train, y_train
    out = model(inputs)
    optimizer.zero_grad()
    loss = criterion(out, labels)
    loss.backward()
    optimizer.step()
    predicted = model.forward(x_train)
    print('epoch{}, loss {}'.format(epoch, loss.item()))


print(model.state_dict())


test = torch.tensor([[0.1], [1.5], [2.3], [3.0], [6.4]])
results = model(test)
for result in results:
    if result <= 0.5:
        print(result, 'false')
    else:
        print(result, 'true')
