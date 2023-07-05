import numpy as np
import typing as tp


def find_nearest_points(a: np.ndarray, b: np.ndarray, k: int) -> np.ndarray:
    a = a.reshape((a.shape[0], 1, a.shape[1]))
    b = b.reshape((1, *b.shape))
    e = np.sum(np.square(b - a), axis=2).T
    e = np.argsort(e, axis=1)
    e = np.vectorize(lambda x: x + 1)(e)
    return e[:, :k]
