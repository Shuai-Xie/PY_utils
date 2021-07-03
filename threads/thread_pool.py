"""
https://tutorialedge.net/python/concurrency/python-threadpoolexecutor-tutorial/
"""
from concurrent.futures import ThreadPoolExecutor
import threading


def task(num):
    print("Task {}".format(num))  # get cur thread identifier
    t = threading.current_thread()
    print(t.name)
    print("Task Executed {}".format(threading.current_thread()))


executor = ThreadPoolExecutor(max_workers=5)

task_number = 10
for i in range(task_number):
    executor.submit(task, i)
