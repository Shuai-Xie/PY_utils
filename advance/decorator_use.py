"""
Decorator 装饰器
为函数执行前后提供功能，但不更改原函数定义
Note:
    1.@functools.wraps(func) 用来包装内部函数
    2.装饰器可多层嵌套，环环深入
    3.本质：将 功能函数 func 作为变量传入 装饰器函数 log 内部
    4.有参装饰器函数，为了使用 @ 语法，才添加了一层包装函数
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


# 装饰器参数，相当于实例化内部的 decorator 函数
def log2(prefix='default'):
    # 内部包裹一个无参装饰器
    def decorator(func):  # 中间层 需要 只传入 func
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
@log2(prefix='inner')
def count(top):
    for i in range(top):
        print(i)


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
# @log2(prefix='player')
def player(top):
    for i in range(top):
        time.sleep(0.2)
        print('\r{}/{}'.format(i + 1, top), end='')
    print()


if __name__ == '__main__':
    player(5)
