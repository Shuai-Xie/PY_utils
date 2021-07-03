# Python 各种下划线：https://zhuanlan.zhihu.com/p/36173202
"""
https://stackoverflow.com/questions/44834/can-someone-explain-all-in-python
It's a list of public objects of that module, as interpreted by import *
_ 开头的 var/func 默认为私有
1. 无法用 import * 引入，使用 __all__ 指定后可以 * 引入
2. 可以用 `my_module._internal_func()` 引入
"""
# __all__ = ['external_func', '_internal_func']


def external_func():
    return 'external_func'


def _internal_func():
    return '_internal_func'


external_var = 1
_internal_var = 0
"""
_var: module 默认的私有成员，不能用 import * 导入，但可用 module._var

var_: 为了和 python 关键字区分

__var: 
类的私有成员，解释器处理后会变成 _Test__var
名称修饰：name mangling，解释器更改变量名称，以便类在扩展时不会产生冲突

__var__：
"""


class Test:
    def __init__(self) -> None:
        self.foo = 1
        self._var = 2
        self.__var = 3  # 私有变量灰色, 被解释器修改为 _Test__var，防止被继承子类(ExtendedTest)修改


t = Test()
print(dir(t))  # 显示对象成员
""" 
['_Test__var', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_var', 'foo']
"""


class ExtendedTest(Test):
    def __init__(self) -> None:
        super().__init__()
        self.foo = 'overridden'
        self._var = 'overridden'
        self.__var = 'overridden'


t2 = ExtendedTest()
print(dir(t2))
""" 
['_ExtendedTest__var', '_Test__var', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_var', 'foo']

注意：'_ExtendedTest__var', '_Test__var', 继承来的私有成员
"""

import struct