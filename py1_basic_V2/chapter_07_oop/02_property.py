"""
属性：
    实例属性
    类属性
"""

"""
实例属性

定义：通过实例.属性名 = 值定义在实例身上的属性，称为：实例属性。

访问：实例.属性名
修改：实例.属性名 = 值
删除：del 实例.属性名
1.每个实例都有自己『独立的一份』实例属性，各个实例之间是互不影响的。
2.实例属性只能通过实例.xxxx访问和修改，不能通过『类名』访问或修改
"""


# 定义一个Person类
class Person:
    # 初始化方法
    def __init__(self, name, age, gender):
        # 通过【实例.属性名 = 值】给实例添加的属性，就叫实例属性
        # 实例属性只能通过实例访问，不能通过类访问
        # 每个实例都有自己【独一份的】实例属性，各个实例之间是互不干扰的
        self.name = name
        self.age = age
        self.gender = gender


print("-----------------实例属性-----------------")
# 创建Person类的实例对象
p1 = Person("张三", 18, "男")
p2 = Person("李四", 22, "女")

# 实例属性只能通过实例访问，不能通过类访问
print(p1.name)
# print(Person.name)


"""
类属性
 在类中直接写赋值语句（例如：a = 100），就会在类身上添加一个a属性，值为 100，
 此时的a就是『类属性』，它属于类本身，由类所拥有，并且该类创建出来的所有实例对象，都能去访问a属性。 

 
1.所有实例访问的，都是同一个类属性，所以类属性通常用于：存放公共数据
2.类属性即可以通过『类』访问，也可以『实例』访问。


"""
print("-----------------类属性-----------------")


# 定义一个Person类
class Person:
    # max_age、planet 他们都是类属性，类属性是保存在类身上的
    # 类属性可以通过类访问，也可以通过实例访问
    # 类属性通常用于保存：公共数据
    max_age = 120
    planet = "地球"

    # 初始化方法
    def __init__(self, name, age, gender):
        # 给实例添加属性
        self.name = name
        self.gender = gender
        # 限制age的最大值
        if age <= Person.max_age:
            self.age = age
        else:
            print(f"年龄超出范围了，已经将年龄设置为最大值：{Person.max_age}")
            self.age = Person.max_age


# 验证一下：类属性是保存在类身上的
print(Person.__dict__)

# 创建Person类的实例对象
p1 = Person("张三", 18, "男")
p2 = Person("李四", 22, "女")

# 验证一下：实例身上是没有类属性的
print(p1.__dict__)
print(p2.__dict__)


# 验证一下：类属性可以通过类访问，也可以通过实例访问
print(Person.max_age)
print(p1.max_age)  # 查找max_age的过程：1.实例自身(p1)  => 2.实例的“缔造者”(Person)
print(p2.planet)

# 测试一下年龄超出范围
p3 = Person("王五", 170, "女")
print(p3.__dict__)


# 注意点：进行【实例.属性名 = 值】操作时，只会对实例自身的属性起作用，不会影响类属性，（有则修改，无则添加）
p1.planet = "火星"
p1.aaa = 100
print(Person.__dict__)
print(p1.__dict__)
print(p2.__dict__)
print(p1.planet)
print(p1.aaa)


print(p2.planet)
