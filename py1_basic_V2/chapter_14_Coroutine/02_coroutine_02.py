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


async def main():
    print("main开始")
    # await去等待一个协程对象（靠自己去编写协程函数，随后调用该函数来得到协程对象）
    res = await work()
    print(res)
    print("main结束")
    return "main的返回值"


result = asyncio.run(main())
print(result)

"""
执行流程图

main() 开始
  ↓
await work()  ← main 挂起，等待 work 完成
  ↓
work() 开始
  ↓
await asyncio.sleep(5)  ← work 挂起，让出 CPU
  ↓
[此时没有其他协程可运行，所以只是等待 5 秒]
  ↓
work() 恢复执行
  ↓
work() 结束，返回结果
  ↓
main() 恢复执行（因为 work 完成了）
  ↓
main() 结束
"""
