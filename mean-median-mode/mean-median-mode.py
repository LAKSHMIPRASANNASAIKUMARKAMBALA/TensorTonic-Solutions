from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    a = np.array(x)

    m = np.mean(a)
    med = np.median(a)
    mode = Counter(x).most_common(1)[0][0]

    data = {
        "mean": float(m),
        "median": float(med),
        "mode": float(mode)
    }

    return data
