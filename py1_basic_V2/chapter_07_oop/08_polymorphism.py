"""
多态

多态就是“多种形态”，即：不同的对象调使用同一个方法名调用方法时，会表现出不同的行为。

# Python中支持：标准多态、鸭子多态
"""

print("---------------------标准多态---------------------")
"""
基于继承实现多态，又叫：『传统多态』或『标准多态』。

常见于Java、C++ 这样的强类型语言中，Python支持『标准多态』。
"""


# 标准多态：
class Animal:
    def speak(self):
        print("动物正在发出声音")


class Dog(Animal):
    def speak(self):
        print("汪汪汪！")


class Cat(Animal):
    def speak(self):
        print("喵喵喵！")


# 注意Pig类没有继承Animal类
class Pig:
    def speak(self):
        print("哼哼哼！----")


# make_sound函数要求：传入的对象，必须是 Animal 类型（或其子类型），才能保证可以调用到sepak方法
def make_sound(animal: Animal):
    animal.speak()


# 创建实例对象
a1 = Animal()
d1 = Dog()
c1 = Cat()

# 多态的体现：同一函数，不同对象 → 不同行为
make_sound(a1)  # 动物正在发出声音
make_sound(d1)  # 汪汪汪！
make_sound(c1)  # 喵喵喵！

# 按标准多态规则：Pig 没有继承 Animal，类型不匹配（会出现类型警告）
p1 = Pig()
make_sound(p1)  # 在其它语言中会报错，虽然 Python 中能运行，但这不属于标准多态


print("---------------------鸭子多态---------------------")
"""
鸭子多态：

鸭子多态，即：『不检查类型』，『不检查继承关系』，只要对象有对应的方法，就可以调用。

Python中的鸭子多态，是『不检查继承关系』，只要对象有对应的方法，就可以调用。


鸭子类型：如果一个东西看起来像鸭子，叫起来也像鸭子，那它就是鸭子，鸭子类型指一种编程风格，它并不依靠查找对象类型，来确定其是否具有正确的实现，而是直接调用或使用其方法或属性。
官方文档地址：https://docs.python.org/zh-cn/3.13/glossary.html#term-duck-typing

特点：不需要继承，只要传进来的对象，有对应实现就可以。
Python 中支持“鸭子多态”。
"""


class Dog:
    def speak(self):
        print("汪汪汪！")


class Cat:
    def speak(self):
        print("喵喵喵！")


class Pig:
    def speak(self):
        print("哼哼哼！")


class Fish:
    def speak(self):
        print("咕噜噜！")


# 不再对animal的类型做限制，animal可以是任何类型，只要能调用speak方法就可以
def make_sound(animal):
    animal.speak()


# 创建实例对象
d1 = Dog()
c1 = Cat()
p1 = Pig()
f1 = Fish()

make_sound(d1)
make_sound(c1)
make_sound(p1)
make_sound(f1)
