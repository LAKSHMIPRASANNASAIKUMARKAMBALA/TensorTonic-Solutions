import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    a=np.array(x)
    b=np.array(p)
    return float(np.sum(a*b))