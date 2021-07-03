import time
import threading


def decrement(n):
    while n > 0:
        n -= 1


def one_thread():
    start = time.time()
    decrement(100000000)
    cost = time.time() - start
    print(cost)


def two_thread():
    start = time.time()

    t1 = threading.Thread(target=decrement, args=[50000000])
    t2 = threading.Thread(target=decrement, args=[50000000])

    t1.start()  # 启动线程，执行任务
    t2.start()  # 同上

    t1.join()  # 主线程阻塞，直到t1执行完成，主线程继续往后执行
    t2.join()  # 同上

    cost = time.time() - start
    print(cost)



if __name__ == '__main__':
    one_thread()  # 4.5244505405426025
    two_thread()  # 4.5370330810546875
