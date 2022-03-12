#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stochastic Calculus

Week 1. Wiener process

@author: boris
"""

import pandas as pd
import numpy as np
import seaborn as sns
from numpy import exp, log, sqrt, max, min
import matplotlib.pyplot as plt


def get_time(T=1, n=1000):
    """    
    Parameters
    ----------
    T : positive float, optional
        Final moment of time. The default is 1.
    n : integer, optional
        Number of increments. The default is 1000.

    Returns
    -------
    Vector of time points.
    """
    return np.linspace(start=0, stop=T, num=n+1)
    
def get_wiener_increments(T=1, n=1000, seed=None):
    """    
    Parameters
    ----------
    T : positive float, optional
        Final moment of time. The default is 1.
    n : integer, optional
        Number of increments. The default is 1000.
    seed : Initial seed for random number generation.
        The default is None.

    Returns
    -------
    Vector of Wiener process increments.
    """
    sd = sqrt(T/n)
    rng = np.random.default_rng(seed)
    delta_W = rng.normal(loc=0, scale=sd, size=n)
    return delta_W


def get_wiener_trajectory(T=1, n=1000, seed=None):
    """    
    Parameters
    ----------
    T : positive float, optional
        Final moment of time. The default is 1.
    n : integer, optional
        Number of increments. The default is 1000.
    seed : Initial seed for random number generation.
        The default is None.

    Returns
    -------
    Vector of (n+1) Wiener process values
    """
    delta_w = get_wiener_increments(T=T, seed=seed, n=n)
    w = np.zeros(n+1)
    w[1:(n+1)] = np.cumsum(delta_w)
    return w


x = get_time(T=5)
y = get_wiener_trajectory(T=5, n=1000, seed=177)

sns.lineplot(x=x, y=y);
plt.savefig('wiener_process.png', dpi=300)


