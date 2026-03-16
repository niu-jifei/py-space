"""
方法:
实例方法、类方法、静态方法
"""

"""
实例方法：

定义：类中所定义的方法，最终会保存在类身上，并且主要是通过实例调用，所以叫：实例方法。
创建：
1.类中定义方法，方法内部第一个参数是self。
2.类中定义方法，方法内部第一个参数是self，self代表的是当前实例对象

特点：
1.实例方法虽然最终会保存在类身上，但它主要是供实例使用的，所以才叫实例方法。
2.因为收到了self参数，所以其内部可以：访问实例属性，调用实例方法。
3.实例方法的主要作用：定义实例对象的具体行为。
"""

from datetime import datetime


# 定义一个Person类
class Person:
    # 初始化方法（给实例添加属性）
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 下面的speak方法、run方法，都保存在类身上，但他们主要是供实例调用，所以他们都叫：实例方法
    # 自定义方法（给实例添加行为）
    def speak(self, msg):
        print(
            f"我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}"
        )

    # 自定义方法（给实例添加行为）
    def run(self, distance):
        print(f"{self.name}疯狂的奔跑了{distance}米")

    # 使用 @classmethod 装饰过的方法，就叫：类方法，类方法保存在类身上的
    # 类方法收到的参数：当前类本身（cls）、自定义的参数
    # 因为收到了cls参数，所以类方法中是可以访问类属性的
    # 类方法通常用于实现：与类相关的逻辑，例如：操作类级别的信息、一些工厂方法
    @classmethod
    def change_planet(cls, value):
        cls.planet = value

    @classmethod
    def create(cls, info_str):
        # 从info_str中获取到有效信息
        name, year, gender = info_str.split("-")
        # 获取当前年份
        current_year = datetime.now().year
        # 计算年龄
        age = current_year - int(year)
        # 创建并返回一个Person类的实例对象
        return cls(name, age, gender)

    # 静态方法
    # 使用 @staticmethod 装饰过的方法，就叫：静态方法，静态方法也是保存在类身上的
    # 静态方法只是单纯的定义在类中，它不会收到：self、cls参数，它收到的参数都是自定义参数
    # 由于静态方法没有收到：self、cls参数，所以其内部不会访问任何：类和实例相关的内容
    # 静态方法通常用于定义：与类相关的工具方法
    @staticmethod
    def is_adult(year):
        # 获取当前的年份
        current_year = datetime.now().year
        # 计算年龄
        age = current_year - year
        # 返回结果（成年True，未成年False）
        return age >= 18

    @staticmethod
    def mask_idcard(idcard):
        return idcard[:6] + "********" + idcard[-4:]


print(
    "---------------------------------------实例方法-----------------------------------------"
)

# 创建Person类的实例对象
p1 = Person("张三", 18, "男")
p2 = Person("李四", 22, "女")

print(Person.__dict__)
print(p1.__dict__)
print(p2.__dict__)

# 通过实例调用实例方法
p1.speak("你好")
p1.run(300)

# 通过类去调用实例方法(能调用，但不推荐)
Person.run(p2, 100)


print(
    "---------------------------------------类方法-----------------------------------------"
)
"""
定义：使用@classmethod装饰器修饰，第一个参数是类本身，通常用形参cls接收。
特点：类方法主要作用：定义与类相关的逻辑。

    
1.可通过『类名』或『实例名』调用，但强烈推荐通过类名调用以体现语义。
2.因为收到了cls参数，所以内部可以访问类属性。
 一般用于：实现与类相关的逻辑，如：操作类级别的信息、工厂方法等
"""

# 验证一下：类方法保存在类身上的
print(Person.__dict__)

# 类方法需要通过类调用
Person.change_planet("月球")
print(Person.__dict__)

# 创建Person实例
p1 = Person("张三", 18, "男")
p2 = Person("李四", 22, "女")

# 验证一下：类属性planet已经修改了
print(p1.planet)
print(p2.planet)

# 测试一下类方法 —— create
p3 = Person.create("李华-2003-女")
print(p3.__dict__)

# 注意点：类方法，也能通过实例调用到，但是非常不推荐
p4 = p1.create("李华-2003-女")
print(p4.__dict__)


print(
    "---------------------------------------静态方法-----------------------------------------"
)

"""
定义：使用@staticmethod装饰器修饰，方法没有self或cls参数，只是单纯的定义在类中。
特点：

    
1.可通过『类名』或『实例名』调用，但强烈推荐通过类名调用以体现语义。 
2.由于没有self或cls参数，所以静态方法中通常：不访问类属性，也不访问实例属性。
3.一般用于：定义与类相关，但可以独立使用的工具方法。
"""
# 验证一下：静态方法也是保存在类身上的
print(Person.__dict__)

# 静态方法需要通过类去调用
result = Person.is_adult(2015)
print(result)
result2 = Person.mask_idcard("212101198802030028")
print(result2)


# 注意点：通过实例也能调用到静态方法，但非常不推荐
p1 = Person("张三", 18, "男")
res = p1.mask_idcard("212101198802030028")
print(res)
