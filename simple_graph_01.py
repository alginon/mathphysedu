# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1);
y = 3*(np.cos(x))**4
plt.plot(x, y)
plt.show()