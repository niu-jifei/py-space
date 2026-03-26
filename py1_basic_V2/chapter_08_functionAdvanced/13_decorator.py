"""
装饰器是一种在【不修改原函数代码】的前提下，对函数进行【增强】的工具

装饰器是一种可调用对象（通常是函数），接收一个函数作为参数，并返回一个新函数。
"""

"""
定义装饰器核心规则：
1.接收被装饰的函数、同时返回新函数（wrapper）
2.装饰器“吐出来”的是 wrapper 函数，以后别人调用的也是 wrapper 函数。
3.为了保证参数的兼容性，wrapper 函数要通过 *args 和 **kwargs 接收参数。
4.wrapper 函数中主要做的是：调用原函数（被装饰的函数）、执行其它逻辑，但要记得将原函数的返回值 return 出去。
"""


# 定义一个装饰器函数
def say_hello(func):
    def wrapper(*args, **kwargs):
        print("你好，我要开始计算了")
        return func(*args, **kwargs)

    return wrapper


"""
使用函数装饰器（手动装饰）
"""


def add(a, b):
    return a + b


def say_hello(func):
    def wrapper(*args, **kwargs):
        print("你好，我要开始计算了~")
        return func(*args, **kwargs)

    return wrapper


# 调用say_hello装饰器，对add函数进行装饰，并得到装饰后的新函数
print("-----使用函数装饰器（手动装饰）-----")
add = say_hello(add)
result = add(1, 2)
print(result)

print("-----使用函数装饰器（语法糖 @）-----")


# 使用函数装饰器（语法糖 @）
@say_hello
def multiply(a, b):
    return a * b


result = multiply(2, 3)
print(result)


print("-----带参数的函数装饰器（三层嵌套）-----")


def say_hello(msg):
    def outer(func):
        def wrapper(*args, **kwargs):
            print(f"你好，我要开始{msg}计算了")
            return func(*args, **kwargs)

        return wrapper

    return outer


# 装饰加法函数
@say_hello("加法")
def add(x, y, z):
    res = x + y + z
    print(f"{x}和{y}和{z}相加的结果是：{res}")
    return res


# 装饰减法函数
@say_hello("减法")
def sub(x, y):
    res = x - y
    print(f"{x}和{y}相减的结果是：{res}")
    return res


# 测试代码
result1 = add(10, 20, 30)
print(result1)

result2 = sub(20, 10)
print(result2)


print("-----多个函数装饰器一起使用-----")
"""
核心：注意装饰顺序，距离函数最近的装饰器，会先工作
"""


def test1(func):
    print("我是test1装饰器")

    def wrapper(*args, **kwargs):
        print("test1追加的逻辑")
        res = func(*args, **kwargs)
        print("test1追加后---的逻辑结束")
        return res

    return wrapper


def test2(func):
    print("我是test2装饰器")

    def wrapper(*args, **kwargs):
        print("test2追加的逻辑")
        res = func(*args, **kwargs)
        print("test2追加后---的逻辑结束")
        return res

    return wrapper


@test1
@test2
def add(x, y):
    res = x + y
    print(f"{x}和{y}相加的结果是{res}")
    return res


result = add(10, 20)
print(result)
