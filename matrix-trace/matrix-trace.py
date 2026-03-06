import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    result = 0
    A = np.array(A)
    if A.shape[0] != A.shape[1]:
            raise ValueError
    else:
        for i in range(A.shape[0]):
            result += A[i][i]
        return result