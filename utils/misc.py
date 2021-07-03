import sys
from datetime import datetime


class Printer:
    def __init__(self, stream=sys.stdout):
        self.terminal = stream

    def print(self, *values, sep=' ', end='\n', time_end=' '):
        """ 模仿 print 输出 多参数，sep，end
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
        """
        curtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.terminal.write(f'[{curtime}]{time_end}')  # add time stamp
        for v in values:
            self.terminal.write(f'{v}{sep}')
        self.terminal.write(end)


class Logger:
    """logger"""
    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'w', encoding='UTF-8')  # 打开时自动清空文件

    def write(self, msg):
        self.terminal.write(msg)  # 命令行打印
        self.log.write(msg)

    def flush(self):  # 必有，不然 AttributeError: 'log' object has no attribute 'flush'
        pass

    def close(self):
        self.log.close()


if __name__ == '__main__':
    print = Printer().print
    print('hello', 123, 'ok')
