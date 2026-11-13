import numpy as np

def vector_sum(a: np.ndarray):
    """Sum elements of 1-D array a without np.sum / loops."""
    n = len(a)
    ones = np.arange(n) * 0.0 + 1.0
    #return np.dot(a,ones)
    return a @ ones
