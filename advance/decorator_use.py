"""
Decorator 装饰器
为函数执行前后提供功能，但不更改原函数定义
"""
from datetime import datetime
import time
import functools


# 简单的装饰器，未传入参数
def log(func):
    """
    :param func: 传入的功能函数
    :return: wrapper 返回函数，以函数对象为变量
    """

    @functools.wraps(func)  # 将 func 原函数的 __name__ 等属性赋值给 wrapper 函数
    def wrapper(*args, **kwargs):
        # 函数执行前后，打印时间
        print(datetime.now())
        func(*args, **kwargs)  # 传入方式不变
        print(datetime.now())

    return wrapper


# 可传入参数的装饰器 [三层函数]，从外到内，层层实例化 [为了使用 @ 语法]
# 其实 log 也可定义参数，但调用时只能 count = log(count, prefix='time')
def log2(prefix='default'):  # 装饰器参数放这里
    # 内部包裹一个无参装饰器
    def decorator(func):
        # 真正 wrapper 的功能
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 函数执行前后，打印时间
            print(prefix, datetime.now())
            func(*args, **kwargs)  # 传入方式不变
            print(prefix, datetime.now())

        return wrapper

    return decorator


# 双重装饰器；将内部 log2 装饰过的函数作为 func 再装饰
@log
@log2(prefix='count')
def count(top):
    for i in range(top):
        time.sleep(0.2)
        print('\r{}/{}'.format(i + 1, top), end='')
    print()


# 显示程序执行时间
def exe_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print('exe time:', t2 - t1)

    return wrapper


@exe_time
@log2(prefix='player')
def player(top):
    for i in range(top):
        time.sleep(0.2)
        print('\r{}/{}'.format(i + 1, top), end='')
    print()


if __name__ == '__main__':
    count(3)

    print(count.__name__)  # wrapper，已变成装饰器最内层的函数名

    player(5)
