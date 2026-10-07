import math
import numpy as np

def cosine_embedding_loss(x1: list, x2: list, label: int, margin: float) -> float:
    a=np.array(x1)
    b=np.array(x2)
    ans=np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
    if(label==1):
        res=1-ans
    elif(label==-1):
        res=max(0,ans-margin)
    return res
