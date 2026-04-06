"""
日志记录，需求如下：
1.用户输入用户名和密码后，程序进行校验：
2.用户名不存在，提示“用户名未注册”，并记录日志。
3.用户名存在，但密码错误，提示“密码错误”，并记录日志。
4.用户名和密码均正确，提示“登录成功”，并记录日志。
"""

import time

# 准备一些用户
users = {"张三": "123456", "李四": "888888", "王五": "abc123"}

# 提示输入信息
username = input("请输入用户名：")
password = input("请输入密码：")

# 获取当前的时间
now = time.strftime("%Y-%m-%d %H:%M:%S")

# 如果用户名不在users中
if username not in users:
    print("用户名未注册")
    with open("log.txt", "at", encoding="utf-8") as file:
        file.write(f"{now}  {username}  登录失败（用户未注册）\n")

# 如果密码不正确
elif users[username] != password:
    print("密码不正确")
    with open("log.txt", "at", encoding="utf-8") as file:
        file.write(f"{now}  {username}  密码错误 \n")

# 登录成功
else:
    print("登录成功！")
    with open("log.txt", "at", encoding="utf-8") as file:
        file.write(f"{now}  {username}  登录成功 \n")
