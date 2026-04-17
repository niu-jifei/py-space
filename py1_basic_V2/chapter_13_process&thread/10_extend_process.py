"""
当子进程逻辑比较复杂，或者想把「进程 + 行为」封装成一个整体时，可以使用继承 Process 类的方式去创建进程，这种方式属于“面向对象风格”


1️⃣核心要点：
 必须继承 Process类
 把子进程要干的事，写进 run() 方法里
 依然使用start方法启动进程，不要手动调用 run()！
 若子进程不需要参数，可以不写__init__，若需要参数，则需编写__init__
 传给的子进程的参数，作为实例属性保存 。
"""

import time
import os
from multiprocessing import Process


class SpeakProcess(Process):

    def __init__(self, a, b, **kwargs):
        super().__init__(**kwargs)
        self.a = a
        self.b = b

    def run(self):
        for index in range(5):
            print(
                f"{self.a}--{self.b}--我在说话{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}"
            )
            time.sleep(1)


class StudyProcess(Process):
    def run(self):
        for index in range(3):
            print(
                f"我在学习{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}"
            )
            time.sleep(1)


if __name__ == "__main__":

    p1 = SpeakProcess(1, 2)
    p2 = StudyProcess()

    p1.start()
    p2.start()

    p1.join()
    p2.join()
