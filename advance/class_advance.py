"""
__slots__ 动态绑定允许 程序运行的过程中 动态给 class 加上功能
"""
from types import MethodType


class Student(object):
    __slots__ = ('name', 'age', 'set_age', 'show_info', 'hello')  # 用 tuple 定义允许绑定的属性名称


def set_age(self, age):
    self.age = age


def show_info(self):
    print(self.name, self.age)


# 传给类的方法必须要有 self
def hello(self):
    print('hello!')


def demo_slots():
    s = Student()
    # 绑定属性 name
    s.name = 'shuai'
    s.age = 24
    # 绑定方法
    s.set_age = MethodType(set_age, s)
    s.show_info = MethodType(show_info, s)
    s.hello = MethodType(hello, s)
    s.set_age(0)
    s.show_info()
    s.hello()


"""
@property 装饰器 将方法变成属性调用
1.既能检查参数，又可以用 类似属性这样简单的方式 来访问类的变量
2.为转变的方法再创建 setter 等装饰器方法，使得变量设置操作等也能用属性方式；
3.如果只有 property，而没有设置 setter，那么就是只读属性
property 方便了调用者 对类对象参数的设置
"""


class Stu(object):

    @property  # 将 getter 方法变成 属性
    def score(self):
        return self._score

    @score.setter
    # @property本身又创建了另一个装饰器 @score.setter，负责把一个setter方法变成属性赋值
    def score(self, value):
        # 数值判断
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


if __name__ == '__main__':
    # demo_slots()
    a = Stu()
    a.score = 90
    print(a.score)
