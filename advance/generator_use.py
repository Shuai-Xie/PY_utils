"""
Generator 生成器
很长的列表，受内存限制；将列表元素按照某种算法推算出来(动态列表)
Note:
    1.generator 推算算法不限于 for 语句
    2.list, tuple, dict 是 Iterable 对象，只有 generator 是 Iterator，能用 next() 索引下一个对象
    3.都可以用 for 遍历
"""

from collections.abc import Iterable  # 防止 DeprecationWarning


def demo():
    # 最简单的定义方法，将列表生成式 [] -> ()
    g = (x * x for x in range(10))
    # print(g)  # <generator object <genexpr> at 0x10e0de950>
    print(isinstance(g, Iterable))  # True

    for item in g:  # 和 list 一样是 iter 对象
        print(item, end=',')


"""
Fibonacci 数列：
f(n+2) = f(n+1) + f(n)
1 = 1 + 0
2 = 1 + 1
3 = 2 + 1
...
"""


# fibonacci 生成器，传入 max，有参的生成器
def fib(max):
    n, a, b = 0, 0, 1  # n: begin
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    print('done')


for item in fib(10):
    print(item, end=' ')


# 杨辉三角
# 生成器函数内可定义任意个 yield 函数
def triangles(max=10):
    l = [1]
    yield l
    n = 1  # 第1行，同样也是 list 的元素个数
    while n < max:
        l = [0] + l + [0]
        l = [l[i] + l[i + 1] for i in range(len(l) - 1)]
        yield l
        n += 1


for res in triangles():
    print(res)
