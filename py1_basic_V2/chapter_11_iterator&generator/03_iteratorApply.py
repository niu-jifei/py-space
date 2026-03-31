"""
迭代器应用
让for循环可以遍历Person的实例对象

"""

print("-----方式一-----")


class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def __iter__(self):
        return PersonIterator(self)


class PersonIterator:
    def __init__(self, person):
        # 将外部传进来的数据保存好
        self.person = person
        # 设置迭代器的初始化状态（指针位置）
        self.index = 0
        # 配置好要遍历的内容
        self.attrs = ["name", "age", "gender", "address"]

    def __iter__(self):
        return self

    def __next__(self):
        # 如果指针的位置超出范围，那就抛出StopIteration异常
        if self.index >= len(self.attrs):
            raise StopIteration
        # 获取要返回的内容
        value = self.attrs[self.index]
        # 更新迭代器状态（指针位置）
        self.index += 1
        return value


print("-----方式一测试-----")
person = Person("张三", 18, "男", "北京")
print(person.__iter__())
personIter = iter(person)
print(personIter.__iter__())
for attr in person:
    print(attr)


print("-----方式二-----")


class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.attrs = ["name", "age", "gender", "address"]
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.attrs):
            raise StopIteration
        value = self.attrs[self.index]
        self.index += 1
        return value


print("-----方式二测试-----")
#  下面的p1既是可迭代对象，又是迭代器
p1 = Person("张三", 18, "男", "北京昌平")
print(p1.__iter__())
print(iter(p1))
for item in p1:
    print(item)


print("-----next()应用-----")
from cn2an import an2cn


class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        # 设置迭代器的初始化状态（指针位置）
        self.__index = 0
        # 配置好要遍历的内容
        self.__attrs = [name, age, gender, address]

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        # 如果指针的位置超出范围，那就抛出StopIteration异常
        if self.__index >= len(self.__attrs):
            raise StopIteration
        # 获取要返回的内容
        value = self.__attrs[self.__index]
        # 将字符串转为大写
        if isinstance(value, str):
            value = value.upper()
        # 将数字转为汉语形式
        if isinstance(value, int):
            value = an2cn(value)
        # 更新迭代器状态（指针位置）
        self.__index += 1
        # 返回value
        return value


# 目标：
# 下面的p1既是可迭代对象，又是迭代器
p1 = Person("zhangsan", 18, "男", "北京昌平")

for item in p1:
    print(item)
