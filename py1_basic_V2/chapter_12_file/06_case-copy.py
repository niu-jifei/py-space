import os

# 源文件
source = "music.mp3"
# 目标目录
target = "D:/media"

# 如果目标目录不存在，那就去创建
if not os.path.isdir(target):
    os.makedirs(target)

with open(source, "rb") as f1, open(target + "/" + "my_music.mp3", "wb") as f2:
    while True:
        # 每次只读取1KB
        data = f1.read(1024)
        # 如果文件读取完毕了，就跳出循环
        if not data:
            break
        # 向目标文件中写入数据
        f2.write(data)
    print("复制完毕")
