"""
创建进程

关于 Process 的参数
在实例化 Process 时，可以传递以下参数：
 🔸group： 默认值为None（应当始终为None）。
 🔸target：子进程要执行的可调用对象，默认值为 None。
 🔸name： 进程名称，默认为 None ，如果设置为 None，Python 会自动分配名字。
 🔸args： 给 target 传的位置参数（元组）
 🔸kwargs：给 target 传的关键字参数（字典）。
 🔸daemon：标记进程是否为守护进程，取值为布尔值（默认为 None，表示从创建方继承）。
备注：可以使用 current_process().name 获取当前进程的名字。


注意：

multiprocessing 模块在 Windows 系统上使用 fork 创建进程时，需要使用 spawn 方式创建进程，需要在 __name__ == '__main__' 内创建子进程

在 Windows 上使用 multiprocessing 时：

操作系统	        进程创建方式	        是否需要 if __name__ == '__main__'
Windows	           spawn（重新导入模块）	✅ 必须
Linux/macOS	       fork（复制内存）	        ❌ 不需要


在 Windows 系统上，multiprocessing 使用 spawn 方式创建子进程，这意味着：
1. 子进程会重新导入主模块
2. 如果没有 if __name__ == '__main__': 保护，会导致无限递归创建进程
3. Python 检测到这个问题并抛出 RuntimeError


Linux/macOS (使用 fork 方式创建进程，不需要这个保护)：
子进程直接复制父进程的内存空间
不会重新导入模块
所以理论上不需要 if __name__ == '__main__': 保护
但是，最佳实践是始终使用这个保护，原因：

代码的可移植性：在 Windows 上也能运行
避免意外问题：某些情况下 fork 也可能有问题
Python 官方推荐：无论什么系统都使用这个保护

建议：无论在什么系统上开发，都养成使用 if __name__ == '__main__': 的习惯，这样代码更具可移植性和健壮性。
"""

import os
import time
from multiprocessing import Process, current_process

print(100, __name__, os.getpid(), os.getppid())
print(101, os.path.abspath(__file__))


# 定义一个 speak 函数，功能是：每隔一秒说话一次（一共说话10次）
def speak():
    for i in range(10):
        print(f"I am speaking..., 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}")
        time.sleep(1)


# 定义一个 study 函数，功能是：每隔一秒学习一次（一共学习15次）
def study():
    for index in range(15):
        print(f"我在学习{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}")
        time.sleep(1)


def speak2(a, b, msg):
    for index in range(10):
        print(
            f"{msg}--{a}--{b}--{current_process().name}--我在说话{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}"
        )
        time.sleep(1)


# # 创建进程对象
# p = Process(target=speak)

# # 启动进程
# p.start()

# # 主进程
# for i in range(10):
#     print(f"I am listening..., 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}")
#     time.sleep(1)


# 注意：一定要写 if __name__ == '__main__' 这个判断，原因如下：
#   1.当创建子进程时，Python 并不会把父进程内存里的 speak 函数直接交给子进程。
#   2.Python会启动一个全新的 Python 解释器进程，重新执行当前的 .py 文件（作为模块）。
#   3.在执行过程中，重新定义出一个 speak 函数，交给子进程。
#
if __name__ == "__main__":
    print("我是主进程中的【第一行】打印")
    # 创建两个 Process 类的实例对象（进程对象），分别是 p1 和 p2。
    # 注意点1：p1 和 p2 就对应着以后的两个子进程，在创建它们的时候，就要指定好他们要执行的任务。
    # 注意点2：此时的 p1 和 p2 只是代码层面的两个进程对象，操作系统还没有创建 p1 和 p2 两个进程。
    p1 = Process(target=speak)
    p2 = Process(target=study)
    p3 = Process(
        target=speak2, name="说话进程2222", args=(666, 888), kwargs={"msg": "尚硅谷"}
    )

    # 调用进程对象的 start 方法，会立刻向操作系统申请一个进程，并且会将该进程交由操作系统进行调度。
    p1.start()
    p2.start()
    p3.start()

    print("我是主进程中的【最后一行】打印")
