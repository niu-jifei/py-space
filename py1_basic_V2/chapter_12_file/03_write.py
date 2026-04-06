"""
写入文件
"""

print("------write模式------")
"""
概述：w模式是写入模式，写入前会先截断文件（清空文件）
"""
with open("b.txt", "wt", encoding="utf-8") as file:
    file.write("你好")


print("------x模式------")
"""
概述：x模式是排它性创建，如果文件已存在，则创建失败。Python会抛出 FileExistsError 异常
"""
# with open("demo.txt", "xt", encoding="utf-8") as file:
#     file.write("你好")


print("------a模式------")
"""
a模式是追加模式，文件指针将会放在文件末尾。
概述：打开文件用于写入，如果文件存在，则在文件末尾追加内容。
"""
with open("a.txt", "at", encoding="utf-8") as file:
    file.write("你好")


print("------flush方法------")
"""
概述：Python 写入文件时，并不是每写一次就立刻落盘，而是：先写到“缓冲区”里。
flush方法：把缓冲区中的数据，立刻写入到文件中。

"""
import time

with open("demo.txt", "at", encoding="utf-8") as file:
    file.write("你好1")
    file.write("你好2")
    file.flush()
    time.sleep(5)
    file.write("你好3")
    file.write("你好4")
