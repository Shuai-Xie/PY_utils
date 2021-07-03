import pandas as pd
import random
import time
import threading
import sys

from utils.misc import Printer

# override print
print = Printer().print

status = {0: 'waiting', 1: 'running', 2: 'finished'}

data = pd.DataFrame({
    "job": ['A', 'A', 'A', 'B', 'B'],
    "task": [1, 2, 3, 1, 2],  # tasks
    "status": [status[0]] * 5
})

# note: 用于控制 estimator 过早结束
# 应对场景：controller 还未添加所有 task, 而 data 已添加的 task 全部 finished
add_all_task = {'A': False, 'B': False}


def wait_a_moment():
    time.sleep(0.01)  # 对于多个线程都更新公共资源 data，防止 bug 有奇效


def controller(identity, job='A', max_task_number=10, add_interval=0.5):
    """add a new task to current job
    Args:
        identity (str): controller name
        job (str, optional): job name. Defaults to 'A'.
        max_task_number (int, optional): max task number of current job. Defaults to 10.
        add_interval (float, optional): add task interval. Defaults to 0.5 second.
    """
    while True:  # 当任务达到 task_max_number 跳出
        wait_a_moment()
        cur_max_task_id = int(data.loc[data['job'] == job, 'task'].max())
        if cur_max_task_id == max_task_number:
            print(f'{identity} add all tasks')
            add_all_task[job] = True  # note: 控制 estimator 退出的关键
            break
        else:
            time.sleep(add_interval)  # 每隔半秒添加1个新任务
            new_task_id = cur_max_task_id + 1
            # 添加 1 行 (所以 list 在外)，续 index; 要返回; 需要 global data
            # data = data.append({'job': job, 'task': new_task_id, 'status': status[0]}, ignore_index=True)
            data.loc[data.shape[0]] = [job, new_task_id, status[0]]  # 行数恰好定位 index + 1
            print(f'{identity} add new task ({job}, {new_task_id})')


def estimator(identity, job='A', running_time=3):
    """schedule and run a waiting task
    Args:
        identity (str): estimator name
        job (str, optional): job name. Defaults to 'A'.
        running_time (int, optional): running time of one task. Defaults to 3.
    """
    def run_task(info, running_time):
        print(f'{info}...')
        time.sleep(running_time)

    while True:
        wait_a_moment()
        # 已完成任务 finished
        if add_all_task[job] and len(data.loc[(data['job'] == job) & (data['status'] != 'finished')].index) == 0:
            print('{} finish all tasks!'.format(identity))
            break

        while True:
            wait_a_moment()  # 面临同时查询问题
            # 可选任务 waiting
            wait_candidates = data.loc[(data['job'] == job) & (data['status'] == 'waiting')].index.tolist()
            if len(wait_candidates) == 0:
                # print(f'{identity} schedule all tasks of job {job}!')  # 太多输出
                break
            else:
                select_id = random.sample(wait_candidates, 1)[0]
                task_name = '({}, {})'.format(job, data.loc[select_id, 'task'])  # (job_id, task_id)
                print('schedule task {} to estimator {}'.format(task_name, identity))
                data.loc[select_id, 'status'] = 'running'

                run_task(f'{identity} running {task_name}', running_time)

                data.loc[select_id, 'status'] = 'finished'  # 多进程可能出现 没有写进去?
                print('finish task {}'.format(task_name))


def watcher(interval=2):
    """watch task status each interval seconds
    Args:
        interval (int, optional): Defaults to 2.
    """
    while True:
        wait_a_moment()
        # print(data, time_end='\n')
        # 按 job - task 都升序输出
        print(data.sort_values(by=['job', 'task'], ascending=[True, True]), time_end='\n')

        if add_all_task['A'] and add_all_task['B'] and len(data.loc[data['status'] != 'finished']) == 0:
            print('ALL FINISHED!')
            break

        time.sleep(interval)


def run():
    WATCH_INTEVAL = 2
    TASK_NUMNER = 10
    ADD_TASK_INTERVAL = 3
    RUNNING_TASK_TIME = 1

    ## watcher
    w = threading.Thread(target=watcher, args=[WATCH_INTEVAL])
    w.start()

    ## controller
    cA = threading.Thread(target=controller, args=['#A', 'A', TASK_NUMNER, ADD_TASK_INTERVAL])
    cB = threading.Thread(target=controller, args=['#B', 'B', TASK_NUMNER, ADD_TASK_INTERVAL])

    cA.start()
    cB.start()

    ## estimator
    numA_threads = 2
    numB_threads = 1
    # eA
    A_threads = []
    for i in range(numA_threads):
        eA = threading.Thread(target=estimator, args=[f'A{i}', 'A', RUNNING_TASK_TIME])
        eA.start()
        A_threads.append(eA)
    # eB
    B_threads = []
    for i in range(numB_threads):
        eB = threading.Thread(target=estimator, args=[f'B{i}', 'B', RUNNING_TASK_TIME])
        eB.start()
        B_threads.append(eB)

    # estimator 执行每个 task 也是异步的，不用阻塞等大家都退出；等各自任务执行完退出即可


if __name__ == '__main__':
    run()