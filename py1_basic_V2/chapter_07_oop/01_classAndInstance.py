# 定义一个Person类（类名通常使用：大驼峰写法）
class Person:

    # 说明：当一个函数被定义在了类中时，那这个函数就被称为：方法。
    # __init__方法：初始化方法，主要作用：给当前正在创建的实例对象添加属性
    # __init__方法收到的参数：当前正在创建的实例对象（self）、其它的自定义参数
    # 当我们以后编写代码去创建Person类实例的时候，Python会自动调用__init__方法
    def __init__(self, name, age, gender):
        # 给实例添加属性（语法为：self.属性名 = 值）
        self.name = name
        self.age = age
        self.gender = gender

    # 自定义方法（给实例添加行为）
    # speak方法收到的参数是：调用speak方法的实例对象（self）、其它参数
    # speak方法只有一份，保存在Person类身上的，所有Person类的实例对象，都可以调用到speak方法
    def speak(self, msg):
        print(f"我叫{self.name}，年龄是{self.age}， 性别是{self.gender}，我想说：{msg}")


# 创建Person的实例对象
p1 = Person("张三", 18, "男")
p2 = Person("李四", 22, "女")


# 通过实例的“点”语法，可以『访问』或『修改』实例的属性
# 通过点语法可以访问或修改实例身上的属性
print(p1.name)
print(p1.age)
print(p1.gender)
print("-" * 20)
print(p2.name)
print(p2.age)
print(p2.gender)
p1.name = "阿三"
print(p1.name)


# 通过实例.__dict__ 的方式，可以查看实例身上的所有属性
print(p1.__dict__)
print(p2.__dict__)


# 实例创建完毕后，依然可以通过 实例.属性名 = 值 去给实例追加属性
p1.address = "北京昌平宏福科技园"
print(p1.__dict__)


# 通过type函数，可以查看某个实例对象，是由哪个类创建出来的
print(type(p1))
print(type(p2))
print(type(Person))
print(type("hello"))


###############################自定义方法#############################
print("---------自定义方法------")
# 验证一下：speak方法是存在Person类身上的
# print(Person.__dict__)

# 创建Person类的实例对象
p1 = Person("张三", 18, "男")
p2 = Person("李四", 22, "女")

# 验证一下：Person的实例对象身上是没有speak方法的
print(p1.__dict__)
print(p2.__dict__)

# 所有Person类的实例对象，都可以调用到speak方法
# 当执行p1.speak()的时候，查找speak方法的过程：1.实例对象自身(p1)  =>  2.实例的“缔造者”的身上(Person)
p1.speak("好好学习")
p2.speak("天天向上")


# 验证一下上述的查找过程
def speak():
    print("巴拉巴拉巴拉巴拉巴拉")


p1.speak = speak
print(Person.__dict__)

p1.speak()
print(p1.__dict__)
print(p2.__dict__)


p1.speak()
p2.speak("aaa")
