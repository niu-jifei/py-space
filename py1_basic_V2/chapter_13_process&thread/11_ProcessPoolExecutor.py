"""
使用进程池的优势：如何使用进程池统一管理多个子进程，避免频繁创建 / 销毁进程带来的开销，
因为进程池会提前创建固定数量的进程，反复使用它们来执行任务。
"""

import os, time
from concurrent.futures import ProcessPoolExecutor, as_completed


def work(n):
    print(f"work正在执行任务{n}.........{os.getpid()}")
    time.sleep(1)
    return f"我是任务{n}的结果"


def work2(n):
    start_time = time.time()
    print(f"work2正在执行任务{n}.........{os.getpid()}")
    if n == 1:
        time.sleep(5)
    elif n == 2:
        time.sleep(3)
    else:
        time.sleep(1)
    return f"我是任务{n}的结果，耗时：{time.time() - start_time:.2f} 秒"


# region
# 1、创建『进程池执行器』、使用 submit 方法提交任务、使用 shutdown 方法等待任务完成。

# if __name__ == "__main__":
#     print("---------start-------------")
#     print(f"主进程：{os.getpid()}")
#     start_time = time.time()
#     # 创建进程执行器
#     executor = ProcessPoolExecutor(3)
#     # 使用 submit 方法提交任务（submit 只负责“提交任务”，不会阻塞主进程）
#     executor.submit(work, 1)
#     executor.submit(work, 2)
#     executor.submit(work, 3)
#     executor.submit(work, 4)
#     executor.submit(work, 5)
#     executor.submit(work, 6)

#     # shutdown 的作用：不再接收新的任务。
#     # wait=True 的作用：阻塞主进程，等待进程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#     print("---------end-------------")
#     print(f"主进程耗时：{time.time() - start_time:.2f} 秒")
# endregion

# region
# 2、获取子进程执行后的返回结果（Future类的实例对象 + result方法）

# if __name__ == "__main__":
#     print("---------start-------------")
#     print(f"主进程：{os.getpid()}")
#     start_time = time.time()
#     # 创建进程执行器
#     executor = ProcessPoolExecutor(3)

#     futures = [executor.submit(work, index) for index in range(1, 6)]

#     # 阻塞主进程，等待进程池中所有任务执行完毕。
#     executor.shutdown(wait=True)

#     for future in futures:  # 获取子进程执行后的返回结果
#         print(future.result())

#     print("---------end-------------")
#     print(f"主进程耗时：{time.time() - start_time:.2f} 秒")
# endregion

# region
# 3、as_completed：按“完成顺序”获取结果

# if __name__ == "__main__":
#     print("---------start-------------")
#     print(f"主进程：{os.getpid()}")
#     start_time = time.time()
#     executor = ProcessPoolExecutor(3)

#     # 使用 submit 方法提交任务（submit 只负责“提交任务”，不会阻塞主进程）
#     futures = [executor.submit(work2, index) for index in range(1, 6)]

#     # 准备一个 result_list 去收集任务的具体结果
#     result_list = []

#     for future in as_completed(futures):
#         result_list.append(future.result())

#     # 阻塞主进程，等待进程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#     # 打印最终的结
#     print(result_list)
#     print("---------end-------------")
#     print(f"主进程耗时：{time.time() - start_time:.2f} 秒")
# endregion

# region
# 4、使用 add_done_callback 方法，为任务添加完成时的回调函数。

# if __name__ == "__main__":
#     print("---------start-------------")
#     print(f"主进程：{os.getpid()}")
#     start_time = time.time()
#     executor = ProcessPoolExecutor(3)

#     # 准备一个 result_list 列表去收集任务的结果
#     result_list = []

#     # 任务完成后的回调函数
#     def done_func(futrue):
#         result_list.append(futrue.result())

#     # 开启7个任务，并指定回调函数
#     for index in range(1, 6):
#         f = executor.submit(work2, index)
#         f.add_done_callback(done_func)

#     # 等所有任务都完成
#     executor.shutdown(wait=True)

#     # 打印最终的结果（按“完成的顺序”获取）
#     print(result_list)

#     print("---------end-------------")
#     print(f"主进程耗时：{time.time() - start_time:.2f} 秒")
# endregion

# region
# 5、使用 map 方法，批量提交任务。
"""
（注意：map方法本身不阻塞，但读取其返回的生成器对象是阻塞的，并且得到结果的顺序，与任务分配的顺序是一致的）
map方法会把这一批任务提交到进程池里执行，它会立刻返回一个生成器，真正的阻塞发生在：生成器取结果时，如 list(result)

"""

# if __name__ == "__main__":
#     print("---------start-------------")
#     print(f"主进程：{os.getpid()}")
#     start_time = time.time()
#     executor = ProcessPoolExecutor(3)

#     # 通过 map 方法批量提交任务（结果按照提交的顺序来）
#     futures = executor.map(work2, range(1, 6))

#     # 获取生成器中的内容
#     print(type(futures))
#     print(list(futures))

#     # 阻塞主进程，等待进程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#     print("---------end-------------")
#     print(f"主进程耗时：{time.time() - start_time:.2f} 秒")
# endregion

# region
# 6、使用 with：进程池的“自动回收”写法，离开 with 代码块时自动执行 shutdown(wait=True)

if __name__ == "__main__":
    print("---------start-------------")
    print(f"主进程：{os.getpid()}")
    start_time = time.time()

    with ProcessPoolExecutor(3) as executor:
        futures = executor.map(work2, range(1, 6))

        print(list(futures))

    print("---------end-------------")
    print(f"主进程耗时：{time.time() - start_time:.2f} 秒")
# endregion
