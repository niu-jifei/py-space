"""

魔法方法
1.在类中定义特殊方法，特殊方法以双下划线开头，以双下划线结尾。
2.特殊方法主要作用：定义实例对象行为


以 __xxx__ 命名的特殊方法（双下划线开头和结尾）。

特点：不需要手动调，在特定场景由 Python 自动调用。


方法	调用时机
1️⃣__str__ 	当调用 print(对象)或str(对象) 时
2️⃣__len__ 	当调用len(对象)时
3️⃣__lt__ 	当执行对象1 < 对象2时
4️⃣__gt__ 	当执行对象1 > 对象2时
5️⃣__eq__ 	当执行对象1 == 对象2时
6️⃣__getattr__	当访问不存在的属性时
"""


# 类中以双下划线开头和结尾的方法，叫魔法方法（魔术方法）。
# 魔法方法不需要手动调用，Python会在特定场景自动调用。
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # __str__ 方法，执行时机：当调用 print(对象)或str(对象) 时
    def __str__(self):
        return f"姓名：{self.name}， 年龄：{self.age}， 性别：{self.gender}"

    # __len__ 方法，执行时机：当调用len(对象)时
    def __len__(self):
        return len(self.__dict__)

    # __lt__方法，执行时机：当执行 对象1 < 对象2 时
    def __lt__(self, other):
        return self.age < other.age

    # __gt__方法，执行时机：当执行 对象1 > 对象2 时
    def __gt__(self, other):
        return self.age > other.age

    # __eq__方法，执行时机：当执行 对象1 == 对象2 时
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # __getattr__方法，执行时机：当访问了对象不存在的属性时
    def __getattr__(self, item):
        print(f"您访问的{item}属性，不存在！")


# 创建Person实例
p1 = Person("张三", 18, "男")
p2 = Person("李四", 22, "女")

# 测试代码
print(p1)
print(str(p1))
print(len(p1))
print(p1 < p2)
print(p1 > p2)
print(p1 == p2)
print(p1.address)
