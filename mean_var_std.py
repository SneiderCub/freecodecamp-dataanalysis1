import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        input = np.array(list).reshape(3,3)
        mean = [input.mean(axis=0).tolist(),input.mean(axis=1).tolist(),input.mean().tolist()]
        variance = [input.var(axis=0).tolist(),input.var(axis=1).tolist(),input.var().tolist()]
        standard_deviation = [input.std(axis=0).tolist(),input.std(axis=1).tolist(),input.std().tolist()]
        max = [input.max(axis=0).tolist(),input.max(axis=1).tolist(),input.max().tolist()]
        min = [input.min(axis=0).tolist(),input.min(axis=1).tolist(),input.min().tolist()]
        sum = [input.sum(axis=0).tolist(),input.sum(axis=1).tolist(),input.sum().tolist()]
        calculations = {
            'mean': mean,
            'variance': variance,
            'standard deviation': standard_deviation,
            'max':max,
            'min':min,
            'sum':sum
}
    return calculations