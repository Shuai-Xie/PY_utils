class Human:
    def __init__(self, sex):
        self.sex = sex

    def p(self):
        print("这是Human的方法")


class Person:
    def __init__(self, name):
        self.name = name

    def p(self):
        print("这是Person的方法")

    def person(self):
        print("这是我person特有的方法")


class Teacher(Person):
    def __init__(self, name, age):
        super(Teacher, self).__init__(name)
        self.age = age


class Student(Human, Person):
    def __init__(self, name, sex, grade):
        # 要想调用特定父类的构造器可以使用父类名.__init__方式
        Human.__init__(self, sex)
        Person.__init__(self, name)
        self.grade = grade


class Son(Human, Teacher):
    def __init__(self, sex, name, age, fan):
        Human.__init__(self, sex)
        Teacher.__init__(self, name, age)
        self.fan = fan


stu = Student("tom", "male", 88)
stu.p()  # 虽然父类Human和Person都有同名P()方法 ，但是调用的是括号里的第一个父类Human的方法
stu.person()
print()

son1 = Son("jerry", "female", 18, "打球")
son1.person()  # 可以调用父类的父类的方法。
son1.p()  # 子类调用众多父类中同名的方法，按继承的顺序查找。
