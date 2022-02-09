#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stochastic Calculus

Week 2. Ito's integral

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



# Draw trajectories of I_t = \int_0^t W_u^3 dW_u

# delta I_u is approximately equal W_u^3 * future delta W


T=1
seed=None
n=1000


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



t = get_time()
integ = get_integral_trajectory(lambda w, t : w**3)

sns.lineplot(x=t, y=integ)


# many trajectories
n_sim = 3
n = 1000
I_matrix = np.zeros((n+1, n_sim))
for i in range(n_sim):
    I_matrix[:, i] = get_integral_trajectory(lambda w, t : w**3, n=n)

I_matrix    

I_df = pd.DataFrame(I_matrix)

t = get_time()
I_df['t'] = t

I_long = I_df.melt(id_vars='t', var_name='trajectory_no', value_name='integral')
I_long

sns.lineplot(y='integral', x='t', hue='trajectory_no', data=I_long, legend=False)


# Variance of an integral
n_sim = 10000
n = 1000
int_values = np.zeros(n_sim)
for i in range(n_sim):
    integral = get_integral_trajectory(lambda w, t : w**3, n=n)
    int_values[i] = integral[n]

int_values    
np.var(int_values)    






