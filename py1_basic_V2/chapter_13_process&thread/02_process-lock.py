"""
Lock（进程锁）
为了防止多个进程同时打印或操作同一资源导致数据错乱，可以使用 Lock

传统用法：
lock.acquire() # 上锁
# ... 临界区代码 ...
lock.release() # 释放锁

上下文管理器用法 (推荐)：
with lock:
    # 自动上锁，退出块时自动释放
    # 好处：即便发生异常也能保证释放锁，避免死锁
"""

# import os
# import time
# from multiprocessing import Process, Lock


# def speak(lock):
#     for index in range(10):
#         # 上锁：如果锁是空闲的，立刻上锁，继续往下执行；如果锁被别人拿着：当前进程会阻塞等待
#         lock.acquire()
#         print("好好", end="")
#         print("学习", end="")
#         print("天天", end="")
#         print("向上")
#         # 释放锁：acquire 和 release 必须成对出现，否则会永远卡住（死等）
#         lock.release()
#         time.sleep(1)


# def study(lock):
#     for index in range(15):
#         # with lock: 会自动完成两件事：
#         #   (1).进入前：自动执行 lock.acquire() 上锁
#         #   (2).离开后：自动执行 lock.release() 释放锁
#         # 好处：即便代码块里发生异常，也能保证释放锁，避免“卡死”
#         with lock:
#             print("A", end="")
#             print("B", end="")
#             print("C", end="")
#             print("D")
#         time.sleep(1)


# if __name__ == "__main__":
#     print("我是主进程中的【第一行】打印")
#     lock = Lock()
#     p1 = Process(target=speak, args=(lock,))
#     p2 = Process(target=study, args=(lock,))
#     p1.start()
#     p2.start()
#     print("我是主进程中的【最后一行】打印")


# 传统 Lock 在面对多次上锁时，会产生死锁状态，解决办法是使用 RLock，示例代码：
import os
import time
from multiprocessing import Process, Lock, RLock


def speak(lock):
    for index in range(10):
        lock.acquire()
        lock.acquire()
        print("好好", end="")
        print("学习", end="")
        print("天天", end="")
        print("向上")
        lock.release()
        lock.release()
        time.sleep(1)


def study(lock):
    for index in range(15):
        with lock:
            print("A", end="")
            print("B", end="")
            print("C", end="")
            print("D")
        time.sleep(1)


if __name__ == "__main__":
    print("我是主进程中的【第一行】打印")
    lock = RLock()
    p1 = Process(target=speak, args=(lock,))
    p2 = Process(target=study, args=(lock,))
    p1.start()
    p2.start()
    print("我是主进程中的【最后一行】打印")
