"""
概念： GIL锁是 CPython 解释器中的一把互斥锁。
作用：无论 CPU 有多少个核心，在某一时刻，只允许同一个进程中的一个线程去执行 Python 代码。
结论：CPython 解释器中的多线程模型，本质上是并发，而不是并行！（是快速切换，而不是同时进行）
为何要这样设计？———— 为了确保解释器级别的数据安全。


GIl 锁何时会被释放？ —— 主动释放（遇到 I/O 操作）、被迫释放（任务超时）
time.sleep()
- 释放 GIL：当线程调用 time.sleep() 时，当前线程会主动释放全局解释器锁（GIL）。
- 线程切换：操作系统会将该线程挂起（进入等待状态），直到睡眠时间结束。在此期间，其他等待 GIL 的线程可以获得锁并执行 Python 字节码。
- 非 busy-wait：sleep 不会占用 CPU 资源进行空转，而是让出 CPU 给其他线程或进程使用。


可以使用多进程来发挥多核 CPU 的性能

结论：GIL 为了确保 Cpython 解释器级别的数据安全，
作为日常编码来说，我们对 GIL 是无感的，
但对于 Lock/Rlock 是实际编码中使用较多的，Lock/Rlock是为了确保业务路基的完整（用于保护共享资源，并发控制）

GIL 限制的是 Python 字节码的并行执行，而不是线程的并发
I/O 操作会释放 GIL，所以多线程在 I/O 密集型任务中仍然很有价值
CPU 密集型任务应该使用多进程（multiprocessing）来绕过 GIL


py 使用 GIL 原因总结：
- 引用计数的线程安全，需要 GIL 保护计数操作，最根本的技术原因
- C 扩展库的兼容性，生态系统的关键考虑
- 历史原因，单核时代的设计选择
- 性能权衡， 单线程性能 vs 并行能力
- 实现简单性，工程实现的考虑



python VS  java

特性	    Python	                Java
内存管理	引用计数 + 垃圾回收	      纯垃圾回收
引用计数	✅ 使用	                ❌ 不使用
GIL 必要性	✅ 保护引用计数	         ❌ 不需要
垃圾回收	辅助机制	              主要机制
线程安全	GIL 自动保护	          需要手动同步


关键区别：
- Python：使用引用计数，需要 GIL 保护计数操作
- Java：不使用引用计数，使用可达性分析，不需要 GIL


Java 不需要 GIL 的原因：
- 不使用引用计数，避免了频繁的计数操作
- 垃圾回收器本身是线程安全的
- 使用可达性分析，而不是引用计数
- 有专门的 GC 线程处理内存回收
"""

import time
from threading import Thread, RLock, current_thread

# Lock / RLock


# region
# Rlock示例1：让打印是完整的
# def show_info1(lock):
#     for index in range(10):
#         with lock:
#             print("尚", end="")
#             print("硅", end="")
#             time.sleep(0.5)
#             print("谷")
#             time.sleep(1)

#         # 不加锁时，打印结果会乱
#         # print("尚", end="")
#         # print("硅", end="")
#         # time.sleep(0.5)
#         # print("谷")
#         # time.sleep(1)


# def show_info2(lock):
#     for index in range(10):
#         with lock:
#             print("at", end="")
#             print("gui", end="")
#             time.sleep(0.5)
#             print("gu")
#             time.sleep(0.5)

#         # 不加锁时，打印结果会乱
#         # print("at", end="")
#         # print("gui", end="")
#         # time.sleep(0.5)
#         # print("gu")
#         # time.sleep(0.5)


# if __name__ == "__main__":
#     lock = RLock()
#     t1 = Thread(target=show_info1, args=(lock,))
#     t2 = Thread(target=show_info2, args=(lock,))
#     t1.start()
#     t2.start()
# endregion


# region
# Rlock示例2：不要让两个窗口卖出同一张票
global count
count = 1


def sale_ticket(lock):
    global count
    with lock:
        if count > 0:
            time.sleep(0.5)
            print(f"当前线程{current_thread().name} 当前当前票号：{count}")
            count -= 1
        else:
            print("票已售罄")

    """
    不加锁的售票逻辑，用于模拟并发问题
    """
    # 1. 检查是否有票
    if count > 0:
        # 2. 模拟处理时间/网络延迟/I/O操作
        # 这一步非常关键：sleep会释放GIL，导致线程切换
        # 此时其他线程可能已经进来了，但count还没减
        time.sleep(0.5)

        # 3. 扣减库存
        # 由于上面sleep期间发生了线程切换，多个线程可能都通过了 if count > 0 的判断
        print(f"当前线程{current_thread().name} 当前票号：{count}")
        count -= 1
    else:
        print(f"当前线程{current_thread().name} 票已售罄")


if __name__ == "__main__":
    lock = RLock()
    for index in range(10):
        t = Thread(target=sale_ticket, args=(lock,))
        t.start()

    # 【重要】等所有线程启动完后，再统一等待它们结束
    # 这样能保证它们在同一时间段内并发执行
    for index in range(10):
        t.join()

    print(f"当前票号：{count}")

# endregion
