import numpy as np

def smallestMultiple (x, y):

    range = np.arange(x, y+1)
    return np.lcm.reduce(range)
