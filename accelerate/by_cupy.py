"""
e.g. https://my.oschina.net/u/4593030/blog/4418756
Doc: https://docs.cupy.dev/en/stable/tutorial/basic.html
    CuPy is a GPU array backend that implements a subset of NumPy interface. numpy 部分接口
"""
import os

# os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'

import numpy as np
import cupy as cp
import time
import functools


# 显示程序执行时间
def exe_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)  # 装饰器函数返回值
        t2 = time.time()
        print('exe time:', t2 - t1)
        return res

    return wrapper


# 创建数据用时比较
@exe_time
def create_arr_cpu():
    return np.ones((500, 1000, 1000))  # 1.8718016147613525


# 数据 size 太大，也会引爆 GPU 内存
# size 越大，cupy 加速性能越明显
@exe_time
def create_arr_gpu():
    return cp.ones((500, 1000, 1000))  # 0.4141056537628174


@exe_time
def multiply(x, y):
    return x * y


def demo_create_mul():
    x_cpu = create_arr_cpu()  # 1.8718016147613525
    x_gpu = create_arr_gpu()  # 0.43718695640563965

    # * 加速 10 倍
    multiply(x_cpu, 5)  # 3.250271797180176
    multiply(x_gpu, 5)  # 0.3008279800415039


# 指定当前使用的 GPU
@exe_time
def demo_set_gpu():
    """ 三种方式
    1. os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    2. with cp.cuda.Device(0):
    3. cp.cuda.Device(0).use()
    """
    # with cp.cuda.Device(0):  # 1 out of memory, 0 work
    #     x_gpu = cp.ones((1000, 1000, 1000))
    #     x_gpu *= 5
    #     print(x_gpu.sum())

    cp.cuda.Device(0).use()
    x_gpu = cp.ones((1000, 1000, 1000))
    x_gpu *= 5
    print(x_gpu.sum())


def demo_data_transfer():
    x_cpu = np.array([1, 2, 3])
    x_gpu = cp.asarray(x_cpu)  # move the data to the current device.
    print(type(x_gpu), x_gpu.device)
    x_cpu = cp.asnumpy(x_gpu)  # move back to host
    print(type(x_cpu))

    with cp.cuda.Device(0):
        x_gpu_0 = cp.array([1, 2, 3])  # create an array in GPU 0
    with cp.cuda.Device(1):
        x_gpu_1 = cp.asarray(x_gpu_0)  # move the array to GPU 1
    print(x_gpu_0.device)  # <CUDA Device 0>
    print(x_gpu_1.device)  # <CUDA Device 1>


if __name__ == '__main__':
    # demo_set_gpu()
    demo_data_transfer()
