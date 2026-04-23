import asyncio
import time

"""
多个任务异步执行

使用asyncio.create_task()方法向事件循环中添加任务，从而实现多个任务异步执行。

（并发执行）：使用 asyncio.gather() 或 asyncio.create_task() 来并发运行多个协程。
"""


# 定义一个协程函数
async def work(n, delay):
    print(f"work{n}开始")
    print(f"work{n}执行中......")
    # 模拟一个IO等待，等待delay秒，会放弃CPU，让出时间片
    await asyncio.sleep(delay)
    print(f"work{n}结束")
    return f"work{n}执行了{delay}秒, 返回值"


async def main():
    print("main开始")
    start = time.time()

    # asyncio.create_task 会把一个协程对象包装成一个可被事件循环调度的任务，并注册到事件循环中
    task1 = asyncio.create_task(work(1, 5))
    task2 = asyncio.create_task(work(2, 5))
    task3 = asyncio.create_task(work(3, 5))

    # 此处会等待task1执行完成
    res1 = await task1
    print(res1)

    # 等待上面的task1完成后，再等待task2完成
    res2 = await task2
    print(res2)

    # 等待上面的task2完成后，再等待task3完成
    res3 = await task3
    print(res3)

    print("main结束", time.time() - start)
    return "我是main的返回值"


# 将协程对象交给事件循环
result = asyncio.run(main())
print(result)
