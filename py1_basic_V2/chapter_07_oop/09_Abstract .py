"""
抽象类

抽象类（Abstract Class） 是一种 不能被直接实例化 的类，通常作为“规范”，
让子类去继承并实现其中定义的抽象方法，本身只定义规范，不需要提供完整实现。


阻止抽象类直接实例化：当一个类继承ABC并包含抽象方法时，Python会禁止直接创建该类的实例。
强制子类实现抽象方法：如果子类未实现所有抽象方法，子类也会被视为抽象类，同样无法实例化。


抽象类的实现步骤
要创建抽象类，需要遵循以下步骤：

从abc模块导入ABC和abstractmethod。
让目标类继承ABC。
使用@abstractmethod装饰器标记抽象方法（方法体通常为pass）。
"""

# 【抽象类】是一种不能直接实例化的类，它通常作为“规范”，让子类去继承，并实现其中定义的【抽象方法】。
from abc import ABC, abstractmethod


# MustRun类一旦继承了ABC类，那MustRun类就是【抽象类】了
class MustRun(ABC):
    # run方法一旦被@abstractmethod装饰后，就变成了【抽象方法】
    @abstractmethod
    def run(self):
        pass

    def speak(self):
        print("我必须说！")


class Person(MustRun):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def run(self):
        print(f"我叫{self.name}，我在努力的奔跑！")


p1 = Person("张三", 18, "男")
p1.run()
p1.speak()


m = MustRun()
m.speak()
