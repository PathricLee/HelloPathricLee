#!/usr/bin/env python
#_*_coding:utf-8_*_


import numpy as np
import matplotlib.pyplot as plt
import math

def sig(x):
    return 1 / (1 + np.exp(-10 * x + 5))

def pao(x):
    return x * x * 2300 / (13815 * 13815)

y = []
h = []
for i in range(13815):
    i += 1
    if i % 500 == 0:
        x = i * 1.0 / 13815
        h.append(i)
        z = int(3605 * sig(x)) + 1000
        y.append(z)


plt.plot(h, y)
plt.show()

str_lst = [str(e) for e in y]
print(', '.join(str_lst))
