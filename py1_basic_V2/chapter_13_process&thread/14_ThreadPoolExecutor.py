"""
线程池

"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import time
from threading import RLock, get_native_id, current_thread


def work(n, lock):
    with lock:
        print(
            f"work正在执行任务{n}.........进程编号：{os.getpid()}， 线程编号：{get_native_id()}, 线程名：{current_thread().name}"
        )
    time.sleep(1)
    return f"我是任务{n}的结果"


def work2(n, lock):

    start_time = time.time()
    # 锁只保护 print 语句
    with lock:
        print(
            f"work2正在执行任务{n}.........进程编号：{os.getpid()}， 线程编号：{get_native_id()}, 线程名：{current_thread().name}"
        )
    # sleep 在锁外面，可以并行执行多个线程
    if n == 1:
        time.sleep(5)
    elif n == 2:
        time.sleep(3)
    else:
        time.sleep(1)
    return f"我是任务{n}的结果，耗时：{time.time() - start_time:.2f} 秒"


# region
# # 1、创建『线程池执行器』、使用 submit 方法提交任务、使用 shutdown 方法等待任务完成。
# if __name__ == "__main__":
#     print("---------start-------------")
#     print(f"主进程：{os.getpid()}")
#     start_time = time.time()
#     # 创建线程执行器
#     executor = ThreadPoolExecutor(3, thread_name_prefix="WorkerThread")
#     lock = RLock()

#     # 使用 submit 方法提交任务（submit 只负责“提交任务”，不会阻塞主进程）
#     future1 = executor.submit(work, 1, lock)
#     future2 = executor.submit(work, 2, lock)
#     future3 = executor.submit(work, 3, lock)
#     future4 = executor.submit(work, 4, lock)
#     future5 = executor.submit(work, 5, lock)
#     future6 = executor.submit(work, 6, lock)

#     # shutdown 的作用：不再接收新的任务。
#     # wait=True 的作用：阻塞主线程，等待线程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#     print(f"---------end------------- 耗时：{time.time() - start_time:.2f} 秒")
# endregion


# region
# 2、获取子线程执行后的返回结果（Future类的实例对象 + result方法）按提交顺序 获取结果
# if __name__ == "__main__":
#     print("---------start-------------")
#     print(f"主进程：{os.getpid()}")
#     start_time = time.time()
#     # 创建线程执行器
#     executor = ThreadPoolExecutor(3, thread_name_prefix="WorkerThread")
#     lock = RLock()

#     # 使用 submit 方法提交任务（submit 只负责“提交任务”，不会阻塞主进程）
#     futures = [executor.submit(work2, index, lock) for index in range(1, 6)]

#     # 遍历 futures 列表，获取每个 Future 实例对象的返回结果
#     for future in futures:
#         print(future.result())

#     # shutdown 的作用：不再接收新的任务。
#     # wait=True 的作用：阻塞主线程，等待线程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#     print(f"---------end------------- 耗时：{time.time() - start_time:.2f} 秒")
# endregion


# region
# 3、使用 as_completed：按“完成顺序”获取结果
# if __name__ == "__main__":
#     print("---------start-------------")
#     print(f"主进程：{os.getpid()}")
#     start_time = time.time()
#     # 创建线程执行器
#     executor = ThreadPoolExecutor(3, thread_name_prefix="WorkerThread")
#     lock = RLock()

#     # 使用 submit 方法提交任务（submit 只负责“提交任务”，不会阻塞主进程）
#     futures = [executor.submit(work2, index, lock) for index in range(1, 7)]

#     # 收集每个线程返回的结果
#     results = []
#     # 将每个线程返回的结果，按完成顺序，添加到 results 列表中
#     for future in as_completed(futures):
#         results.append(future.result())

#     for result in results:
#         print(result)

#     # shutdown 的作用：不再接收新的任务。
#     # wait=True 的作用：阻塞主线程，等待线程池中所有任务执行完毕。
#     executor.shutdown(wait=True)

#     print(f"---------end------------- 耗时：{time.time() - start_time:.2f} 秒")
# endregion


# region
# 4、使用 add_done_callback 方法，为任务添加完成时的回调函数
# if __name__ == "__main__":
#     print("---------start-------------")
#     print(f"主进程：{os.getpid()}")
#     start_time = time.time()
#     # 创建线程执行器
#     executor = ThreadPoolExecutor(3, thread_name_prefix="WorkerThread")
#     # 创建线程锁
#     lock = RLock()

#     # 收集每个线程的执行结果
#     result_list = []

#     # 定义一个线程执行成功后的回调函数
#     def done_func(f):
#         result_list.append(f.result())

#     # 使用submit提交任务，并指定回调函数
#     for index in range(1, 8):
#         f = executor.submit(work2, index, lock)
#         f.add_done_callback(done_func)

#     # shutdown 的作用：不再接收新的任务。
#     # wait=True 的作用：阻塞主线程，等待线程池中所有任务执行完毕。
#     executor.shutdown(wait=True)

#     for result in result_list:
#         print(result)

#     print(f"---------end------------- 耗时：{time.time() - start_time:.2f} 秒")
# endregion


# region
# 5、map
"""
使用 map 方法批量提交任务（注意：map方法本身不阻塞，但读取其返回的生成器对象是阻塞的，并且得到结果的顺序，与任务分配的顺序是一致的）
map方法会把这一批任务提交到线程池里执行，它会立刻返回一个生成器，真正的阻塞发生在：生成器取结果时，如 list(result)

"""
# if __name__ == "__main__":
#     print("---------start-------------")
#     print(f"主进程：{os.getpid()}")
#     start_time = time.time()
#     # 创建线程执行器
#     executor = ThreadPoolExecutor(3, thread_name_prefix="WorkerThread")
#     # 创建线程锁
#     lock = RLock()

#     # 使用 map 方法批量提交任务
#     result = executor.map(work2, range(1, 8), [lock] * 7)

#     for i in list(result):
#         print(i)

#     # shutdown 的作用：不再接收新的任务。
#     # wait=True 的作用：阻塞主线程，等待线程池中所有任务执行完毕。
#     executor.shutdown(wait=True)

#     print(f"---------end------------- 耗时：{time.time() - start_time:.2f} 秒")
# endregion

# region
# 6、使用 with：线程池的“自动回收”写法，离开 with 代码块时自动执行 shutdown(wait=True)
if __name__ == "__main__":
    print("---------start-------------")
    print(f"主进程：{os.getpid()}")
    start_time = time.time()
    # 创建线程执行器
    with ThreadPoolExecutor(3, thread_name_prefix="WorkerThread") as executor:

        # 创建线程锁
        lock = RLock()

        result = list(executor.map(work2, range(1, 8), [lock] * 7))

        for i in result:
            print(i)

    print(f"---------end------------- 耗时：{time.time() - start_time:.2f} 秒")
# endregion
