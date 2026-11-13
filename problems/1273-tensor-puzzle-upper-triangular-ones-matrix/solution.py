import numpy as np

def triu_ones(n: int) -> np.ndarray:
    """n x n upper-triangular matrix of ones (including diagonal)."""
    idx = np.arange(n)
    rows = idx[:, None]
    cols = idx[None, :]
    return (rows<=cols).astype(np.float64)
