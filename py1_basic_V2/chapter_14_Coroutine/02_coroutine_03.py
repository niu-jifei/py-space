import asyncio


async def work():
    print("work开始")
    print("work执行中......")
    # await去等待一个协程对象（靠asyncio.sleep方法，返回一个协程对象）
    """
    asyncio.sleep 会让出 CPU，让出 CPU，让出时间片
    事件循环检查是否有其他就绪的协程
    此时 main 协程正在 await work()，它是挂起状态，不是就绪状态
    没有其他协程可运行，所以只能等待 5 秒
    """
    res = await asyncio.sleep(5, result="睡眠结束了")
    print(res)
    print("work结束")
    return "工作结果"


async def other_task():
    print("其他任务开始")
    await asyncio.sleep(2)
    print("其他任务结束")
    return "其他任务结果"


async def main():
    print("main开始")
    # await去等待一个协程对象（靠自己去编写协程函数，随后调用该函数来得到协程对象）
    # res = await work()
    # 同时运行多个协程,并发执行，多个协程同时运行
    res = await asyncio.gather(work(), other_task())
    print(res)
    print("main结束")
    return "main的返回值"


result = asyncio.run(main())
print(result)

"""
执行流程图

main开始
work开始
work执行中......
其他任务开始
其他任务结束      # 2秒后
睡眠结束了       # 5秒后
work结束
['工作结果', '其他任务结果']
main结束
main的返回值
"""
