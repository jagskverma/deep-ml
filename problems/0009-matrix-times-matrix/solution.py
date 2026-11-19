# Cell 1
import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if not a or not b:
        return -1
    if any(len(row) != len(b) for row in a):
        return -1  
    return (np.array(a) @ np.array(b)).tolist()