import numpy as np
import typing as tp


def find_max_sum_segment(a: tp.List[int], k: int) -> int:
    b = np.ones(len(a))
    b = np.repeat(b, len(a))
    b = b.reshape((len(a), len(a)))
    b = np.triu(b, 0) - np.triu(b, k)
    b = b @ a
    return max(b[0:len(a) - k + 1])

