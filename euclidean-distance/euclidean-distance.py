import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    return float(
        np.linalg.norm(np.array(x)-np.array(y))
    )