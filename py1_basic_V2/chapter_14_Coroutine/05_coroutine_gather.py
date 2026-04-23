import asyncio
import time


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

    # 把多个协程对象同时丢给事件循环，并在全部执行完后，一次性拿到所有结果。
    # gather 会等待所有传入的协程完成，并返回它们的结果列表
    result = await asyncio.gather(work(1, 2), work(2, 2), work(3, 2))
    print(result)

    # 打印每个任务的结果
    for res in result:
        print(res)

    print("main结束", time.time() - start)
    return "我是main的返回值"


# 将协程对象交给事件循环
result = asyncio.run(main())
print(result)
