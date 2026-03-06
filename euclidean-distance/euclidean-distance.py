import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    result = 0.0
    x = np.array(x)
    y = np.array(y)
    if x.shape != y.shape:
        raise ValueError
    m= x.shape[0]
    for i in range(m):
        result += ((x[i] - y[i]) ** 2)
    return result ** (1/2)