import numpy as np

def triplet_loss(anchor: list, positive: list, negative: list, margin: float = 1.0) -> float:
    x=np.atleast_2d(np.asarray(anchor, dtype=float))
    y = np.atleast_2d(np.asarray(positive, dtype=float))
    z = np.atleast_2d(np.asarray(negative, dtype=float))

    res=np.sum((x-y)**2,axis=1)
    ans=np.sum((x-z)**2,axis=1)
    losses=np.maximum(0,res-ans+margin)
    return float(np.mean(losses))