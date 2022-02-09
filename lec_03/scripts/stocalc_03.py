#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stochastic Calculus

Week 3. SDE solution

@author: boris
"""

import pandas as pd
import numpy as np
import seaborn as sns
from numpy import exp, log, sqrt, max, min


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



def get_integral_trajectory(integrand_fun, T=1, n=1000, seed=None):
    delta_w = get_wiener_increments(T=T, seed=seed, n=n)
    w = np.zeros(n+1)
    w[1:(n+1)] = np.cumsum(delta_w)
    t = get_time(T=T, n=n)
    integrand = integrand_fun(w, t)
    
    delta_integral = integrand[0:n] * delta_w
    
    integral = np.zeros(n+1)
    integral[0] = 0
        
    integral[1:(n+1)] = np.cumsum(delta_integral)

    return integral


T=1
n=1000
seed=None
def get_sde_trajectory(integrand_dw, integrand_dt, T=1, n=1000, seed=None, y0=0):
    delta_w = get_wiener_increments(T=T, seed=seed, n=n)
    w = np.zeros(n+1)
    w[1:(n+1)] = np.cumsum(delta_w)
    
    t = get_time(T=T, n=n)
    dt = T/n
    
    y = np.zeros(n+1)
    y[0] = y0
    
    for i in range(n):
        delta_y = integrand_dw(y[i], w[i], t[i]) * delta_w[i] + integrand_dt(y[i], w[i], t[i]) * dt
        y[i+1] = y[i] + delta_y

    return y

T = 1
n = 10000
y = get_sde_trajectory(lambda y, w, t : 0.02 * y, lambda y, w, t : 0.03 * y, y0=100, T=T, n=n)
t =  get_time(T=T, n=n)

r = get_sde_trajectory(lambda r, w, t : 0.01, lambda r, w, t : 0.05 - r, y0=0.07, n=n)

sns.lineplot(x=t, y=y)

for i in range(5):
    print(i)


