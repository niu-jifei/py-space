"""
内存地址分析

内存分为两个部分：栈内存、堆内存；变量在栈内存中，对象在堆内存中。


Python 中变量里保存的不是存数据，而是指向堆中对象的引用（内存地址）。


不可变对象：重新赋值会创建新对象
int 类的实例对象，是不可变对象，所以修改变量 a 时，会创建新对象，不会影响其他引用（b）
Python 中常见的不可变对象有：int 、float 、bool 、str 、tuple 、frozenset 、None。
Python 中常见的可变对象有：list 、dict 、set 、自定义类的实例对象。


可变对象：修改内容不改变地址

自定义类对象的内存表示
"""

a = 66
print(id(a))
print(hex(id(a)))

b = 66
print(id(b))
print(hex(id(b)))
print(a is b)


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


print(hex(id(Person)))
p1 = Person("张三", 18, "男")
print(hex(id(p1)))
p2 = Person("张三", 18, "男")
print(hex(id(p2)))
print(p1 is p2)
