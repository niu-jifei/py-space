"""
访问控制

属性赋予三种权限，分别是：公有属性、受保护属性、私有属性



权限类型	定义方式	类当前类内部访问	在子类内部访问	 在类外部访问
公有属性	属性名	    ✅ 能	        ✅ 能	        ✅ 能
受保护属性	_属性名	    ✅ 能	        ✅ 能	        ⚠️ 能（但不推荐）
私有属性	__属性名	✅ 能	        ❌ 不能	        ❌ 不能
"""


class Person:
    def __init__(self, name, age, idcard):
        self.name = name  # 公有属性：当前类内部、子类内部、类外部，可都可访问
        self._age = age  # 受保护属性：当前类内部、子类内部，可以访问
        self.__idcard = idcard  # 私有属性：仅能在当前类内部访问

    def speak(self):
        # 类的内部，可以访问任何权限的属性（公有属性、受保护属性、私有属性）。
        print(f"我叫：{self.name}，年龄：{self._age}，身份证：{self.__idcard}")


class Student(Person):
    def hello(self):
        # 子类的内部可以访问：公有属性、受保护属性
        print(f"我是学生，我叫：{self.name}，年龄：{self._age}")


p1 = Person("张三", 18, "110101199001011234")
print(p1.name)

# 类的外部，仅能访问公有属性
# 注意：如果在类的外部，强制访问【受保护的属性】，也能访问，但最好别这么做
print(p1._age)

# 强制访问【私有属性】会报错
# print(p1.__idcard)

# 扩展：Python保护【私有属性】的方式，是重命名，例如：__idcard属性，会被重命名为：_Person__idcard
print(p1.__dict__)
print(p1._Person__idcard)


print("---------------getter 与 setter----------")
"""
getter：读取属性的方法
setter：修改属性的方法

通过@property和@xxx.setter语法，把普通方法变成像属性一样使用的方法。

"""


class Person:
    def __init__(self, name, age, idcard):
        self.name = name  # 公有属性：当前类内部、子类内部、类外部，可都可访问
        self._age = age  # 受保护属性：当前类内部、子类内部，可以访问
        self.__idcard = idcard  # 私有属性：仅能在当前类内部访问

    # 注册 age 属性的 getter 方法：当访问 Person 实例的 age 属性时，age方法会自动调用
    @property
    def age(self):
        return self._age

    # 注册 age 属性的 setter 方法：当给 Person 实例的 age 属性赋值时，age方法会自动调用
    @age.setter
    def age(self, value):
        if value <= 120:
            self._age = value
        else:
            print("年龄非法，已将年龄变为最大值120")
            self._age = 120

    # 注册 idcard 属性的 getter 方法：当访问 Person 实例的 idcard 属性时，会自动调用此方法
    @property
    def idcard(self):
        return self.__idcard[:6] + "********" + self.__idcard[-4:]

    # 注册 idcard 属性的 setter 方法，当 idcard 被修改时调用，内部会禁止修改身份证号并给出提示。
    @idcard.setter
    def idcard(self, value):
        print("抱歉，身份证号不允许随意修改，如有特殊需求，请联系管理员！")


p1 = Person("张三", 18, "110101199001011234")
print(p1.age)
print(p1.idcard)

# 测试修改age
p1._age = 19
print(p1.age)

p1.age = 99
print(p1.age)

# 测试修改idcard
p1.idcard = "asd"
