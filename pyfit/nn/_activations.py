"""
Activation functions
"""

import numpy as np
from pyfit import Tensor


def tanh(x: Tensor) -> Tensor:
    return np.tanh(x)


def tanh_prime(x: Tensor) -> Tensor:
    y: Tensor = tanh(x)
    return 1 - y ** 2