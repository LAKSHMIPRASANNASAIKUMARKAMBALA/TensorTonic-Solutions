import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    x=np.array(a)
    y=np.array(b)
    norm_x=np.linalg.norm(x)
    norm_y=np.linalg.norm(y)
    ans = np.dot(x,y) / (np.linalg.norm(x)*np.linalg.norm(y))
    if(norm_x==0 or norm_y==0):
        return 0.0
    
    return float(ans)