"""
类装饰器


1.包含__call__方法的类，就是类装饰器。
2.像调用函数一样，去调用类装饰器的实例对象，就会触发__call__方法的调用。
3.__call__方法通常接收一个函数作为参数，并且会返回一个新函数。
"""


def add(x, y):
    return x + y


print("-----定义类装饰器-----")


class SayHello:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("hello")
            return func(*args, **kwargs)

        return wrapper


print("-----使用类装饰器（手动装饰）-----")

# 使用 SayHello 去装饰 add 函数（手动装饰）
say = SayHello()
add = say(add)

result = add(1, 2)
print(result)


print("-----使用类装饰器（语法糖 @）-----")


@SayHello()
def multiply(a, b):
    return a * b


print(multiply(2, 3))


print("-----使用类装饰器（带参数）-----")


class SayHello:
    def __init__(self, msg):
        self.msg = msg

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(self.msg)
            return func(*args, **kwargs)

        return wrapper


@SayHello("hello")
def subtract(a, b):
    return a - b


print(subtract(5, 3))


print("-----多个类装饰器一起使用-----")
"""
和之前的函数装饰器一样，离函数近的装饰器，先工作。
"""


# 多个类装饰器的使用
class Test1:
    def __call__(self, func):
        print("我是Test1装饰器")

        def wrapper(*args, **kwargs):
            print("我是Test1追加的逻辑")
            result = func(*args, **kwargs)
            print("Test1追加后---的逻辑结束")
            return result

        return wrapper


class Test2:
    def __call__(self, func):
        print("我是Test2装饰器")

        def wrapper(*args, **kwargs):
            print("我是Test2追加的逻辑")
            result = func(*args, **kwargs)
            print("Test2追加后---的逻辑结束")
            return result

        return wrapper


@Test1()
@Test2()
def add(x, y):
    res = x + y
    print(f"{x}和{y}相加的结果是{res}")
    return res


result = add(10, 20)
print(result)
