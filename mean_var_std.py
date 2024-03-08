import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        input = np.array(list).reshape(3,3)
        mean = [input.mean(axis=0).tolist(),input.mean(axis=1).tolist(),input.mean().tolist()]
        variance = [input.var(axis=0).tolist(),input.var(axis=1).tolist(),input.var().tolist()]
        calculations = {
            'mean': mean,
            'variance': variance
            }
    return calculations