import numpy as np

def diag(A: np.ndarray) -> np.ndarray:
    """Return the main diagonal of square matrix A."""
    n = A.shape[0]
    return A.flatten()[::n+1]
