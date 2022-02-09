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



get_wiener_trajectory()



T = 2
n = 1000
seed = 777
data = pd.DataFrame({'t': get_time(T, n), 'W': get_wiener_trajectory(T, n, seed=seed)})

data['wp_drift'] = 2 * data['t'] + 4 * data['W']
data['exp_wp'] = exp(data['wp_drift'])

data
sns.lineplot(data=data, x='t', y='exp_wp')



# many trajectories
n_sim = 10 
n = 1000
W_matrix = np.zeros((n+1, n_sim))
for i in range(n_sim):
    W_matrix[:, i] = get_wiener_trajectory(n=n)

W_matrix    

W_df = pd.DataFrame(W_matrix)

t = get_time()
W_df['t'] = t

W_long = W_df.melt(id_vars='t', var_name='trajectory_no', value_name='w')
W_long

sns.lineplot(y='w', x='t', hue='trajectory_no', data=W_long, legend=False)

# What is the probability that W_t will hit 3 before T=2?

n_sim = 10000
n_success = 0
for _ in range(n_sim):
    w = get_wiener_trajectory(T=2, n=1000)
    if max(w) > 3:
        n_success += 1
        
n_success / n_sim

# Average time to hit 0.2 or -0.4 for W_t?
n_sim = 10000
sum_of_times = 0
T = 3
n = 1000
for _ in range(n_sim):
    w = get_wiener_trajectory(T=T, n=n)
    where = np.where((w > 0.2) | (w < -0.4))
    if where[0].size == 0:
        new_time = T
    else:
        new_time = min(where[0]) * T / n
    sum_of_times += new_time

sum_of_times / n_sim

