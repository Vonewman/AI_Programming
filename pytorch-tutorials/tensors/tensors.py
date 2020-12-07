import torch


def sigmoid(x):
    """ Sigmoid activation function

    Arguments
    ---------
    x: torch.Tensor
    """
    return 1/(1 + torch.exp(-x))


# Generate some data
torch.manual_seed(7)
features = torch.randn((1, 5))
weights = torch.randn_like(features)
bias = torch.randn((1, 1))


print("Calculate the output of this network using the weights and bias.\n")
out = sigmoid(torch.sum(features * weights) + bias)
print(out)


print()
print("\n")
print()


print("Calculate the output of this network using matrix multiplication.\n")
out2 = sigmoid(torch.mm(features, weights.view(5, 1)) + bias)
print(out2)
