# 嵌套 & 递归

# 函数嵌套调用测试1
def greet(name, msg):
    print(f'我叫{name}，我想说的话在下面：')
    speak(msg)
    print('嗯，我想说的结束了')

def speak(msg):
    print('----------')
    print(msg)
    print('----------')

greet('张三', '你好啊')

# 递归
# 使用递归打印n次“你好啊”（从大到小）
def welcome(n):
    print(f'你好啊{n}')
    if n > 1:
        welcome(n - 1)
# 调用函数
welcome(5)


# 使用递归求阶乘
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
# 调用函数，求5的阶乘
result = factorial(6)
print(result)


def add(n1, n2):
    """
    计算两个数相加的结果
    :param n1:第一个数
    :param n2:第二个数
    :return:二者相加的结果
    """
    return n1 + n2

result = add(1, 2)