"""
Inter-Process Communication - 进程间通信

使用 Queue 实现进程间通信

"""

import time
import os
from multiprocessing import Queue, Process, current_process


# 子进程1：往队列里放数据
def queue_put(q):
    for i in range(5):
        print(
            f"【queue_put()】, {os.getpid()} -> {current_process().name} 放入元素==》{i}"
        )
        q.put(i)
        time.sleep(0.5)


# 子进程2：从队列里取数据
def queue_get(q):
    for index in range(5):
        data = q.get()
        print(
            f"【queue_get()】, {os.getpid()} -> {current_process().name} 取出数据：{data}"
        )
        time.sleep(1)


"""
备注：q 是在主进程中创建的，但可以被子进程使用，因为 multiprocessing.Queue是跨进程的。
为什么数据不会乱掉？ —— 因为队列是先进先出的。

"""
if __name__ == "__main__":
    q = Queue()

    p1 = Process(target=queue_put, args=(q,))
    p2 = Process(target=queue_get, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
