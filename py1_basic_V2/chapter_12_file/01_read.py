"""
读取文件
"""

print("------read方法-------")
"""
1.read(size)中的size是可选参数。
 🔸若不传递size参数，表示：读取文件中所有的内容（注意内存占用！）。
 🔸若传递了size参数，表示：读取文件中指定个数的字符，或指定大小的字节。

 
read会从上一次read的位置继续读取，若到达文件末尾后继续读取，将返回空字符串
"""
# 第一步：创建『文件对象』
# 完整写法
# file = open(file='a.txt', mode='rt', encoding='utf-8')


"""
即使文件存在于脚本所在目录，如果 Python 运行时的工作目录（working directory）与脚本所在目录不一致，使用相对路径 "a.txt" 就会找不到文件。
使用绝对路径可以确保无论从哪个目录运行脚本，都能正确找到文件。


修改说明：

添加了 import os 导入模块
使用 os.chdir(os.path.dirname(os.path.abspath(__file__))) 将工作目录切换到脚本所在目录
保持使用相对路径 "a.txt"，代码更加简洁
工作原理：

os.path.abspath(__file__) 获取脚本的绝对路径
os.path.dirname() 获取脚本所在目录
os.chdir() 切换到该目录
这样相对路径 "a.txt" 就能正确指向脚本目录下的 a.txt 文件

"""
import os

# 切换工作目录到脚本所在目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 完整写法
# file = open(file='a.txt', mode='rt', encoding='utf-8')

# 简写
file = open("a.txt", "rt", encoding="utf-8")

# 使用绝对路径读取
# file = open('D:/test/atguigu.txt', 'rt', encoding='utf-8')

# 读取二进制文件
# file = open('D:/test/girl.jpg', 'rb')

# 第二步：操作文件（读取）
# 多次调用read去逐步读取文件
r1 = file.read(2)
r2 = file.read(3)
r3 = file.read(4)
r4 = file.read()
print(r1, end="")
print(r2, end="")
print(r3, end="")

print("继续读取文件...")
print(r4, end="")


# 用循环配合多次read（对内存友好）
while True:
    result = file.read(10)
    if result == "":
        break
    print(result, end="")

# 第三步：关闭文件
file.close()


print("-----readline方法-----")
"""
概述：使用文件对象的readline方法，读取文件中的一行

1.readline(size) 中的size是可选参数。
 🔸若不传递size参数，表示：读取当前这一行所有的内容。
 🔸若传递了size参数，表示：表示读取当前行时，最多能读取的字符数，或字节数
 🔸注意：size不是行数。
2.readline方法，也是从上一次位置继续读取，若到达文件末尾后继续读取，返回空字符串。

"""

# 第一步：创建『文件对象』
file = open("a.txt", "rt", encoding="utf-8")


r = file.readline(20)
print(f"读取到的内容：{r.strip()}")

# 第二步：操作文件（读取）
# 依次调用readline逐行读取
r1 = file.readline()
r2 = file.readline()
r3 = file.readline()
r4 = file.readline()
print(r1.strip())
print(r2.strip())
print(r3.strip())
print(r4.strip())

# 通过循环配合readline逐行读取
while True:
    line = file.readline()
    if line == "":
        break
    # print(line.strip())
    print(line, end="")


# 第三步：关闭文件
file.close()


print("-----for 循环遍历文件对象-----")
"""
概述：可以使用for循环直接遍历文件对象（逐行遍历）
"""
# 第一步：创建『文件对象』
file = open("a.txt", "rt", encoding="utf-8")

# 第二步：操作文件（读取）
for line in file:
    print(line, end="")

# 第三步：关闭文件
file.close()


print("-----readlines方法-----")
"""
概述：使用文件对象的readlines方法，一次性按“行”读完，返回一个列表


方法说明：

    
1.readlines(hint) 中的hint是可选参数。
 🔸若不传递hint参数，表示：读取当前文件的所有行。
 🔸若传递了hint参数，表示：期望读取的【字符个数 或 字节数】（hint不是行数）。
2.注意：由于readlines是一次性读取文件的所有内容，所以不适合读取体积较大的文件。

"""
# 第一步：创建『文件对象』
file = open("a.txt", "rt", encoding="utf-8")

# 第二步：操作文件（读取）
result = file.readlines()
print(result)

# 第三步：关闭文件
file.close()
