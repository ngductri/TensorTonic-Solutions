import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    v = np.array(v)
    D = np.zeros((v.shape[0], v.shape[0]))
    for i in range(D.shape[0]):
        D[i][i] = v[i]
    return D
