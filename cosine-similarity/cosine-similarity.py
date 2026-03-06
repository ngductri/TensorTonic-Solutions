import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)

    dot_product = a @ b
    A = np.linalg.norm(a)
    B = np.linalg.norm(b)
    if ( A * B) == 0:
        return 0.0
    cos_ = dot_product / (A * B)
    return cos_