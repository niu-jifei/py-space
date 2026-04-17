print("------rt+模式------")
"""
概述：r模式可以读取，+模式可以更新（读取或写入），所以rt+模式可读可写。
注意：r模式打开文件后，文件指针在起始位置。
备注：由于t是默认值，所以rt+中的t可以省略。
"""

import os

# 切换工作目录到脚本所在目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))


with open("rt.txt", "rt+", encoding="utf-8") as file:
    # seek(offset, whence)方法：用于改变文件对象指针的位置，参数说明如下：
    #   offset：偏移量，要移动多少距离，字节偏移量
    #   whence：参考点，从哪里开始计算偏移，有三种取值：
    #       0：从文件开头计算（默认值）
    #       1：从当前位置计算
    #       2：从文件末尾计算
    #  注意：在文本模式下，不要随意去定位中文字符位置，否则可能破坏文件编码。
    file.seek(0, 0)
    file.write("你好")


print("------wt+模式------")
"""
概述：w模式可以写入，+模式可以用于更新（读取或写入），所以wt+模式可读可写。
注意：w模式打开文件后，文件指针在起始位置，但write方法执行完后，指针在文件结束位置。
备注：由于t是默认值，所以wt+中的t可以省略。
"""

with open("wt.txt", "wt+", encoding="utf-8") as file:
    file.write("你好")
    file.seek(0, 0)
    result = file.read()
    print(result)


print("------xt+模式------")
"""
概述：x模式可以写入，+模式可以用于更新（读取或写入），所以xt+模式可读可写。
注意：x模式打开文件后，文件指针在起始位置。
"""
# with open("xt.txt", "xt+", encoding="utf-8") as file:
#     file.write("你好")
#     file.seek(0, 0)
#     result = file.read()
#     print(result)

print("------at+模式------")
"""
概述：a模式可以追加内容，+模式可以用于更新（读取或写入），所以at+模式可读可写。
注意：a模式打开文件后，文件指针在结束位置。
备注：由于t是默认值，所以at+中的t可以省略。
"""
with open("at.txt", "at+", encoding="utf-8") as file:
    file.write("你好")
    file.seek(0, 0)
    result = file.read()
    print(result)
