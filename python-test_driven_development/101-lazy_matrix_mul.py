#!/usr/bin/python3
"""Module 101-lazy_matrix_mul.

Provides a function that multiplies 2 matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the product of the matrices m_a and m_b.

    Uses numpy.matmul and lets NumPy raise errors."""
    return np.matmul(m_a, m_b)
