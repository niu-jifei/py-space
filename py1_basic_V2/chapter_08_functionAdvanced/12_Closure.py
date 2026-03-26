"""
闭包
闭包 = 内层函数 + 被内层函数引用的外层变量

什么是闭包？

产生闭包的三个条件如下：
1.必须有函数嵌套
2.内层函数使用了外层函数的变量
3.外层函数返回内层函数


闭包的作用

1. 函数的参数可以传入函数
2. 函数的返回值可以返回函数
3. 函数的参数可以传入函数的返回值
4. 函数的返回值可以返回函数的参数
"""


def outer():
    num = 10

    def inner():
        nonlocal num
        num += 1
        print(num)

    return inner


f = outer()
f()  # 11
f()  # 12
f()  # 13

print(f.__closure__)
print(f.__code__.co_freevars)
print(f.__closure__[0].cell_contents)

print("--------闭包是如何保存外层变量的？--------")
"""
外层变量会被保存到 闭包单元（cell）中，例如下面代码中，
那些被 inner函数所使用到的outer函数中的局部变量，
会被封存在闭包单元（cell） 中，这些cell组成一个 __closure__ 元组，保存在了inner函数上。 

不会保留 outer 中所有变量，只会保存inner中所用到的。
"""


def outer():
    num = 10
    print(id(num))  # 140707460170952
    msg = "你好啊！"
    print(id(msg))

    def inner():
        nonlocal num
        num += 1
        print(num)

    return inner


f = outer()

print(
    f.__closure__
)  # __closure__的值是一个元组，元组中保存着被inner函数所“挽救”下来的数据
print(type(f.__closure__))
for i in f.__closure__:  # 迭代元组中的元素
    print(i.cell_contents)
print(f.__closure__[0].cell_contents)  # 10
print(id(f.__closure__[0].cell_contents))  # 140707460170952


"""

"""
print("-----1. 每次获得一个新闭包，互不影响（闭包之间是互相独立的）-----")


def outer():
    num = 10

    def inner():
        nonlocal num
        num += 1
        print(num)

    return inner


f1 = outer()
f1()
f1()
f1()
print("*****************")
f2 = outer()
f2()


print("-----2. 外层变量为可变对象时仍互不影响。-----")


def outer():
    nums = []

    def inner(value):
        nums.append(value)
        print(nums)

    return inner


# 每次调用 outer() 都创建一个新的 nums
f1 = outer()
f1(10)
f1(20)
f1(30)
print("**********************")
f2 = outer()
f2(666)

print("-----闭包的优点-----")
"""
1.可以“记住”状态：不用全局变量，也不用写类，就能在多次调用之间保存数据。
2.可以做“配置过的函数”：先传一部分参数，把环境固定住，得到一个定制版函数。
3.可以实现简单的“数据隐藏”：外层变量对外不可见，只能通过内层函数访问。
4.是装饰器（decorator）等高级用法的基础。
"""


def beauty(char, n):
    def show_msg(msg):
        print(char * n + msg + char * n)

    return show_msg


show1 = beauty("*", 3)
show1("你好啊")
show1("尚硅谷")

show2 = beauty("@", 5)
show2("你好啊")
show2("尚硅谷")


print("-----闭包的缺点-----")
"""
1.理解成本较高：对初学者不太友好，滥用会让代码难读。
2.如果闭包里引用了很大的对象，又长期不释放，可能会增加内存占用。
很多场景下，其实用【类 + 实例属性】会更清晰，闭包不一定是最优解
"""


class Beauty:
    def __init__(self, char, n):
        self.char = char
        self.n = n

    def show_msg(self, msg):
        print(self.char * self.n + msg + self.char * self.n)


b1 = Beauty("*", 3)
b1.show_msg("你好啊")
b1.show_msg("尚硅谷")

b2 = Beauty("#", 5)
b2.show_msg("你好啊")
b2.show_msg("尚硅谷")
