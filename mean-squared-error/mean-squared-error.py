import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    a=np.array(y_pred)
    b=np.array(y_true)
    n=a.size
    ans=(np.mean((a-b)**2))
    return ans