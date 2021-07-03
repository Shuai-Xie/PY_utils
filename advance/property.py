"""
property, setter and getter
https://medium.com/bryanyang0528/python-setter-%E5%92%8C-getter-6c08a9d37d46 
"""


class gundam(object):
    def __init__(self, driver):
        self._driver = driver

    @property
    def driver(self):  # 本质上，是将 get_driver() 方法，换了名字后，变得属性可获取
        return self._driver

    def set_driver(self, new_driver):
        self._driver = new_driver


# 使用 setter 好处
# 1.使用 property 隐藏了实际的保护和私有变量名；外边包装了一层
# 2.方便给私有变量赋值；并不要求 init 的变量名和 property 相同，二者是分开的


class gundam(object):
    def __init__(self, driver_name):
        self.driver = driver_name  # 在这里已经调用了 property 的 setter 方法

    @property
    def driver(self):  # 本质上，是将 get_driver() 方法，换了名字后，变得属性可获取
        print('getter')
        return self._driver

    @driver.setter  # property (getter) 对应的 setter 函数
    def driver(self, new_driver):
        print('setter')
        self._driver = new_driver


if __name__ == '__main__':
    a = gundam('me')  # init 时，因为初始化方式，已经调用了属性的 setter 方法
    print(a.driver)
    a.driver = 'he'  # 再次 调用属性对应的 setter 方法
    print(a.driver)