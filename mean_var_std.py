import numpy as np

def calculate(value):
    if len(value) < 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(value).reshape(3, 3)

    mean = [
        np.mean(matrix, axis=0).tolist(),
        np.mean(matrix, axis=1).tolist(),
        np.mean(matrix)
    ]

    variance = [
        np.var(matrix, axis=0).tolist(),
        np.var(matrix, axis=1).tolist(),
        np.var(matrix)
    ]

    std_deviation = [
        np.std(matrix, axis=0).tolist(),
        np.std(matrix, axis=1).tolist(),
        np.std(matrix)
    ]

    mmax = [
        np.max(matrix, axis=0).tolist(),
        np.max(matrix, axis=1).tolist(),
        np.max(matrix)
    ]

    mmin = [
        np.min(matrix, axis=0).tolist(),
        np.min(matrix, axis=1).tolist(),
        np.min(matrix)
    ]

    msum = [
        np.sum(matrix, axis=0).tolist(),
        np.sum(matrix, axis=1).tolist(),
        np.sum(matrix)
    ]

    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_deviation,
        'max': mmax,
        'min': mmin,
        'sum': msum,
    }

    return calculations
