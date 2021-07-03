from concurrent.futures import ThreadPoolExecutor, TimeoutError
from threading import Thread
import time


def demo_result_timeout():
    def foo(sleep_time):
        print('sleep', sleep_time)
        time.sleep(sleep_time)

    with ThreadPoolExecutor() as executor:
        sleep_time = 2
        future = executor.submit(foo, sleep_time)
        try:
            future.result(timeout=sleep_time - 1)  # timeout 控制 yes/no
            print(future.running())
            print('yes')
        except TimeoutError:
            print('no')


def demo_join_timeout():
    def foo(sleep_time):
        print('sleep', sleep_time)
        time.sleep(sleep_time)

    sleep_time = 2
    t = Thread(target=foo, args=[sleep_time])
    t.start()
    t.join(timeout=sleep_time - 1)
    print(t.is_alive())  # thread is still running, if not join in time
    print('cancel if not finished in time')  # todo can't find a lightweight way

    if t.is_alive():  # if finished, will thread will die
        print('no')
    else:
        print('yes')


demo_result_timeout()
# demo_join_timeout()