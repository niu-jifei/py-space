"""
继承Thread创建线程
"""

import os, time
from threading import get_native_id, Thread, RLock


class SpeakThread(Thread):
    def __init__(self, lock, **kwargs):
        super().__init__(**kwargs)
        self.lock = lock

    def run(self):
        for index in range(5):
            with self.lock:
                print(
                    f"1---我在说话{index} >>>>> 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}, 线程名称:{self.name}"
                )
                print(
                    f"2---我在说话{index} >>>>> 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}, 线程名称:{self.name}"
                )
            time.sleep(1)


class StudyThread(Thread):
    def __init__(self, lock, **kwargs):
        super().__init__(**kwargs)
        self.lock = lock

    def run(self):
        for index in range(5):
            with self.lock:
                print(
                    f"1---我在学习{index} ----- 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}, 线程名称:{self.name}"
                )
                print(
                    f"2---我在学习{index} ----- 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}, 线程名称:{self.name}"
                )
            time.sleep(1)


if __name__ == "__main__":
    print(f"-------start------- 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}")
    lock = RLock()

    t1 = SpeakThread(lock, name="SpeakThread")
    t2 = StudyThread(lock, name="StudyThread")

    # 调用线程对象的 start 方法，会立刻将该线程交由操作系统进行调度。
    t1.start()
    t2.start()

    # 让主线程等 t1和t2 线程执行完毕后，主线程再继续执行。
    t1.join()
    t2.join()

    print(f"-------end------- 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}")
