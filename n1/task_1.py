import numpy as np
import typing as tp


def matrix_multiplication(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return (a.reshape((*a.shape, 1)) * b.reshape((1, *b.shape))).sum(axis=1)

