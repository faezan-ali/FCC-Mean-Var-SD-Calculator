import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    x = np.reshape(list, (3,3))
    calcs = {}

    calcs["mean"] = [np.mean(x, axis=0).tolist(), np.mean(x, axis=1).tolist(), np.mean(x)]
    calcs["variance"] = [np.var(x, axis=0).tolist(), np.var(x, axis=1).tolist(), np.var(x)]
    calcs["standard deviation"] = [np.std(x, axis=0).tolist(), np.std(x, axis=1).tolist(), np.std(x)]
    calcs["max"] = [np.max(x, axis=0).tolist(), np.max(x, axis=1).tolist(), np.max(x)]
    calcs["min"] = [np.min(x, axis=0).tolist(), np.min(x, axis=1).tolist(), np.min(x)]
    calcs["sum"] = [np.sum(x, axis=0).tolist(), np.sum(x, axis=1).tolist(), np.sum(x)]

    return calcs
