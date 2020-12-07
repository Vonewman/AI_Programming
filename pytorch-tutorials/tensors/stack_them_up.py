import torch


def sigmoid(x):
    """
    Sigmoid activation function

        Arguments
        ---------
        x: torch.Tensor
    """
    return 1/(1 + torch.exp(-x))


# Generate some data
torch.manual_seed(7)
features = torch.randn((1, 3))
n_input = features.shape[1]
n_hidden = 2
n_output = 1
# Weights for hidden layer
W1 = torch.randn(n_input, n_hidden)
# Weights for hidden layer to output layer
W2 = torch.randn(n_hidden, n_output)
# Bias terms for hidden and output layers
B1 = torch.randn((1, n_hidden))
B2 = torch.randn((1, n_output))


h = sigmoid(torch.mm(features, W1) + B1)
output = sigmoid(torch.mm(h, W2) + B2)
print("The output for this multi-layer network is {} ".format(output))
