import numpy as np

def seno(x):
    return np.sin(x)

def coseno(x):
    return np.cos(x)

def tangente(x):
    return np.tan(x)

def exponencial(x, y):
    return x**y

def logaritmo(x):
    return np.log2(x)

def h(x):
    y = np.zeros(len(x))
    for idx, x in enumerate(x):
        if x>=0:
            y[idx]=1.0
    return y