import numpy as np

def sample_var_std(x: list) -> dict:
    a=np.array(x)
    mean=np.mean(a)
    var=float(np.var(a,ddof=1))
    std=float(np.std(a,ddof=1))
    data={"variance":var,
         "standard_deviation":std}
    return data