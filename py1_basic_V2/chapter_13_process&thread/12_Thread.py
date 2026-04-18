"""
进程中至少都有一个线程


主进程里的主线程

线程是进程中的执行单位：
一个进程里，至少有一个线程（主线程）
一个进程里，也可以有多个线程
多个线程之间会： 共享进程的内存空间、 但执行顺序由操作系统调度



threading.Lock

Lock（锁） 是 Python 线程同步机制，用于解决多线程竞争共享资源的问题。

RLock（可重入锁） 与普通 Lock 的区别：
- RLock 允许同一个线程多次获取同一个锁（可重入）
- 普通 Lock 不允许同一线程重复获取，会导致死锁


使用 with lock: 可以确保：

- 同一时间只有一个线程能执行 print 语句
- 输出内容不会被交错打断
- 保证线程安全
with lock:      # 获取锁（如果锁被其他线程占用，会等待）
    print(...)  # 临界区代码（互斥执行）
                # 自动释放锁



threading.RLock vs multiprocessing.RLock
它们虽然名字相同，但作用范围和底层实现完全不同

核心区别
特性	    threading.RLock	      multiprocessing.RLock
作用范围	同一进程内的多个线程	不同进程之间
内存空间	共享同一进程内存	    跨进程（需要特殊机制）
底层实现	基于线程本地存储	    基于系统级进程同步原语
适用场景	多线程编程	           多进程编程
性能	    快（同一进程内）	   较慢（跨进程通信）


threading.RLock（线程锁）
```python
from threading import RLock

lock = RLock()

def func():
    with lock:
        # 临界区代码
        pass
```
工作原理：同一进程内的线程共享这个锁对象
内存共享：所有线程都能访问同一个 lock 对象
速度：快，因为不需要跨进程通信

multiprocessing.RLock（进程锁）
```python
from multiprocessing import RLock

lock = RLock()

def func(lock):
    with lock:
        # 临界区代码
        pass

if __name__ == "__main__":
    p = Process(target=func, args=(lock,))
    p.start()
```
工作原理：通过操作系统级别的进程同步机制实现
跨进程：锁对象会被序列化/反序列化传递给子进程
速度：较慢，因为涉及进程间通信（IPC）


为什么需要两个不同的 RLock？
根本原因：内存隔离
线程用 threading 的锁，进程用 multiprocessing.RLock


### 可重入锁
Lock（普通锁）- 写一个
RLock（可重入锁）- 写多个


特性	        Lock	             RLock
可重入性	    ❌ 不可重入	         ✅ 可重入
重复 acquire	❌ 死锁	            ✅ 允许
计数器	         无	                  有（记录 acquire 次数）
release次数	     必须=acquire 次数	  必须 = acquire 次数
性能	         稍快	              稍慢（维护计数器）
适用场景	     简单互斥	          递归/嵌套/复杂场景

"""

import os
import time
from threading import get_native_id, RLock, Thread


def speak(lock):
    for index in range(5):
        with lock:  # 自动 acquire + release
            print(
                f"1---我在说话{index} >>>>> 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}"
            )
            print(
                f"2---我在说话{index} >>>>> 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}"
            )
        time.sleep(1)

        # 不加锁，会导致线程安全问题，输出内容会被交错打断，导致结果不正确
        # print(
        #     f"1---我在说话{index} >>>>> 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}"
        # )
        # print(
        #     f"2---我在说话{index} >>>>> 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}"
        # )
        # time.sleep(1)


def study(lock):
    for index in range(5):
        with lock:
            print(
                f"1---我在学习{index} ----- 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}"
            )
            print(
                f"2---我在学习{index} ----- 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}"
            )
        time.sleep(1)


if __name__ == "__main__":
    print(f"-------start------- 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}")
    lock = RLock()

    """
    Thread 的参数：
    group： 默认值为 None（应当始终为 None）。
    target： 子线程要执行的可调用对象，默认值为 None。
    name： 线程名称，默认为 None。如果设置为 None，Python 会自动分配名字
    args： 给 target 传的位置参数（元组）。
    kwargs： 给 target 传的关键字参数（字典）。
    daemon： 标记线程是否为守护线程，取值为布尔值（默认为 None）。
    
     """

    # 使用 Thread 创建线程对象
    t1 = Thread(target=speak, args=(lock,))
    t2 = Thread(target=study, args=(lock,))

    # 调用线程对象的 start 方法，会立刻将该线程交由操作系统进行调度。
    t1.start()
    t2.start()

    # 让主线程等 t1 和 t2 线程执行完毕，主线程再继续执行
    t1.join()
    t2.join()

    print(f"-------end------- 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}")
