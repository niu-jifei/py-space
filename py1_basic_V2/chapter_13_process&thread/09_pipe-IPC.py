"""
Inter-Process Communication - 进程间通信

使用 Pipe 实现进程间通信


Pipe 就像一根“水管”，一头负责发送，另一头负责接收。

# 创建管道
# Pipe() 会返回两个连接对象，它们分别代表管道的两端。
# duplex用于控制管道为单向还是双向，True表示双向，False表示单向   duplex 双工
con1, con2 = Pipe(duplex=True)

# 单向 Pipe 的规则：con1只能发送，con2只能接收。



发送与接收
send方法： 向管道中发送数据。
recv方法： 从管道中接收数据。
"""

import time
import os
from multiprocessing import Pipe, Process, current_process


def put(con1):
    for i in range(5):
        print(f"【put()】, {os.getpid()} -> {current_process().name} 放入元素==》{i}")
        con1.send(i)
        time.sleep(0.5)


def get(con2):
    for i in range(5):
        data = con2.recv()
        print(f"【get()】, {os.getpid()} -> {current_process().name} 取出数据：{data}")
        time.sleep(1)


if __name__ == "__main__":
    con1, con2 = Pipe(duplex=True)

    p1 = Process(target=put, args=(con1,))
    p2 = Process(target=get, args=(con2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
