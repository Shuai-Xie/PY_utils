"""
https://docs.python.org/3/library/string.html#grammar-token-conversion

format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
    fill            ::=  <any character>
    align           ::=  "<" | ">" | "=" | "^"
    sign            ::=  "+" | "-" | " "   带符号输出
    width           ::=  digit+
    grouping_option ::=  "_" | ","
    precision       ::=  digit+
    type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

format 函数
https://www.runoob.com/python/att-string-format.html
"""


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)


if __name__ == '__main__':
    # print(Point(1, 2))

    # print('{:+f}; {:+f}'.format(3.14, -3.14))  # +3.140000; -3.140000
    print('{:.3f}; {:.3f}'.format(3.14, -3.14))  # 3.140; -3.140
    print('{:<.3f}'.format(3.14))
    print('{:>10.3f}'.format(3.14))  # 长度10，右对齐
    print('{:0>10.3f}'.format(3.14))  # 长度10，右对齐，补0
