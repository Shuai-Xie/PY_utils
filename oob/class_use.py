"""
OOP Object Oriented Programming
类：抽象的模板
实例：根据模板实例化的对象，方法相同，但各自拥有数据不同

OOB 三个基本概念：数据封装、继承和多态

1.数据封装
    成员变量 访问控制，私有变量 __name -> _Student__name
    dir 获取 类对象的所有属性和方法，其中 __xxx__ 的属性和方法在 Python 中都是有特殊用途
2.继承与多态
    多个子类 Dog, Cat 对同一父类 Animal 继承
    静态语言 vs 动态语言; 动态语言的 "鸭子类型" 不要求严格的类型继承
"""


class Student:

    # 构造函数：把创建实例时一些必要属性强制输入
    def __init__(self, name, score, male='m'):
        # 成员变量 访问限制
        # python 解释器将 __name 转变成 _Student__name 所以不能外部访问
        self.__name = name  # __ 开头的变量 -> 私有变量
        self.__score = score
        self.male = male  # 公有，类实例可访问

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def print_score(self):
        print(self.__score)


# 类的继承
class Undergraduate(Student):
    def __init__(self, name, score, male, college):
        super().__init__(name, score, male)
        self.__college = college

    # 重载方法
    def print_score(self):
        print('college:', self.__college)
        super().print_score()

    def print_new_score(self):
        print(self._Student__name)  # 不建议这样使用


def demo_extend():
    a = Student('shuai', 90)
    a.print_score()
    print(a._Student__score)

    b = Undergraduate('shuai', 100, 'm', 'ZJU')
    b.print_score()


"""
多态 polymorphic
"""


class Animal:
    def run(self):
        print('Animal is running')


class Cat(Animal):
    def run(self):
        print('Cat is running')


class Dog(Animal):
    def run(self):
        print('Dog is running')


class Person:
    def run(self):
        print('Person is running')


def demo_poly():
    animals = [Animal(), Cat(), Dog(), Person()]
    # 多态性：同一 run 方法展现不同的功能
    for a in animals:
        a.run()


if __name__ == '__main__':
    demo_extend()
    # demo_poly()

    # a = Undergraduate('shuai', 100, 'm', 'ZJU')
    #
    # # dir 获取类对象的所有属性和方法
    # # for item in dir(a):
    # #     print(item)
    #
    # # 其中 __xxx__ 的属性和方法在 Python 中都是有特殊用途，常常是 buildins
    # # 以下两个方法等价
    # setattr(a, 'male', 'f')
    # a.print_score()
    # a.__setattr__('male', 'm')  # 更加面向对象
    # a.print_score()
