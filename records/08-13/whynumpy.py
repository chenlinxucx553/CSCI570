__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/13/2020 11:51 AM'

import numpy as np
from timeit import timeit
from numpy.lib.stride_tricks import as_strided

# Adapted from Alex Rogozhnikov (linked below)

# Generate array of (fake) closing prices
prices = np.random.randn(100)

# We want closing prices from the ten days prior
window = 10
# Create array of closing prices to predict
y = prices[window:]


def make_X1():
    # Create array of zeros the same size as our final desired array
    X1 = np.zeros([len(prices) - window, window])
    # For each day in the appropriate range
    for day in range(len(X1)):
        # take prices for ten days from that day onwards
        X1[day, :] = prices[day:day + window]
    return X1


def make_X2():
    # Save stride (num bytes) between each item
    stride, = prices.strides
    desired_shape = [len(prices) - window, window]
    # Get a view of the prices with shape desired_shape, strides as defined, don't write to original array
    X2 = as_strided(prices, desired_shape, strides=[stride, stride], writeable=False)
    return X2


print(timeit(make_X1))  # 56.7 seconds
print(timeit(make_X2))  # 7.7 seconds, over 7x faster!
