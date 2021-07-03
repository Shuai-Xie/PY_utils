"""
https://zhuanlan.zhihu.com/p/60994299
"""
import numpy as np
import numba as nb
import time


@nb.jit()
def nb_sum(a):
    Sum = 0
    for i in range(len(a)):
        Sum += a[i]
    return Sum


# 没用numba加速的求和函数
def py_sum(a):
    Sum = 0
    for i in range(len(a)):
        Sum += a[i]
    return Sum


a = np.linspace(0, 100, 10000)

t1 = time.time()
py_sum(a)
t2 = time.time()
print(t2 - t1)

t1 = time.time()
nb_sum(a)
t2 = time.time()
print(t2 - t1)
