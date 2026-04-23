# 定义一个协程函数
# 异步 I/O（非阻塞）
async def work():
    print("work开始")
    print("work执行中......")
    print("work结束")
    return "工作结果"


# 调用协程函数，会得到协程对象
coroutine_object = work()


# 将协程对象交给asyncio.run()，asyncio.run()会将协程对象包装成一个任务交给事件循环。
# asyncio.run 方法做了3件事：
#   1.创建一个事件循环。
#   2.将收到的协程对象，包装成一个任务（task），交给事件循环。
#   3.启动事件循环。
# 注意：asyncio.run 会阻塞当前线程，直到任务执行完毕，并返回该任务 return 的最终结果。


import asyncio

result = asyncio.run(coroutine_object)
print(result)
