import asyncio
import time

"""
多个任务同步执行

（串行执行）：如果确实需要串行，需要依次 await 每个协程。

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

    # 创建3个协程对象
    coroutine1 = work(1, 5)
    coroutine2 = work(2, 5)
    coroutine3 = work(3, 5)

    # 此处会等待 corutine1 执行完成
    res1 = await coroutine1
    print(res1)

    # 等待 corutine1 完成后，再等待 corutine2 完成
    res2 = await coroutine2
    print(res2)

    # 等待 corutine2 完成后，再等待 corutine3 完成
    res3 = await coroutine3
    print(res3)

    print(f"main结束，耗时：{time.time() - start}秒")
    return "main的返回值"


# 将协程对象交给事件循环
res = asyncio.run(main())
print(res)
