import order
import pay


import copy  # 拷贝对象（浅拷贝、深拷贝）
import os  # 操作系统相关操作（文件、文件夹、路径系统层面的操作）
import random  # 随机数相关（生成随机数、随机选择、洗牌）

# 上面的copy、os、random是标准库模块中的【非内置模块】，可以通过__file__查看文件位置
print(copy.__file__)
print(os.__file__)
print(random.__file__)

# 如下的这些模块，属于内置模块（无法看到具体实现，也没有__file__属性）
# 存根文件，没有做具体的实现，只是提供了大概说明
import time  # 时间相关操作（获取时间、延时、格式化时间等。）
import math  # 数学相关（开平方、取绝对值 等等）
import sys  # Python 解释器相关操作

# print(time.__file__)

# 创建一个文件夹
# os.mkdir("demo")

# 随机选择一个人
names = ["张三", "李四", "王五", "李华"]
print(random.choice(names))

# 洗牌
names = ["张三", "李四", "王五", "李华"]
random.shuffle(names)
print(names)

# 休眠
time.sleep(2)
print("ok")

# 获取当前时间
print(time.strftime("%H:%M:%S"))
print(time.strftime("%p %I:%M:%S"))

# 开平方
print(math.sqrt(4))

# 取绝对值
print(math.fabs(-11.2))

# 获取Python解释器的版本
print(sys.version)
