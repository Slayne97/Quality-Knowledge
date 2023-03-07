# Gradient descent for linear regression
# yhat = wx + b
# loss = (y-yhat)**2 / N
# Initialize some parameters
# Create gradient descent function
# Iteratively make updates


import numpy as np

x = np.random.randn(10, 1)
y = 2*x + np.random.rand()
w = 0.0
b = 0.0
learning_rate = 0.0


def descend(x, y, w, b, learning_rate):
    dldw = 0.0
    dldb = 0.0
    N = x.shape[0]

    for xi, yi in zip(x,y):
        dldw = 


for epoch in range(400):




