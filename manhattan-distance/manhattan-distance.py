import numpy as np

def manhattan_distance(x: list, y: list) -> float:
   return float(np.sum(np.abs(np.array(x)-np.array(y))))