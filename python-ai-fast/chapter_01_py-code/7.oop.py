# 案例演示：Python 的类和对象，面向对象编程

# 1. 基本类定义和对象创建
print("=== 基本类定义和对象创建 ===")
class Person:
    # 类属性
    species = "人类"
    
    # 初始化方法/构造函数
    def __init__(self, name, age, gender):
        # 实例属性
        self.name = name
        self.age = age
        self.gender = gender
        print(f"创建了Person对象: {name}")
    
    # 实例方法
    def introduce(self):
        return f"我叫{self.name}，今年{self.age}岁，性别{self.gender}"
    
    # 类方法
    @classmethod
    def get_species(cls):
        return f"我们都是{cls.species}"
    
    # 静态方法
    @staticmethod
    def is_adult(age):
        return age >= 18

# 创建对象
person1 = Person("张三", 25, "男")
person2 = Person("李四", 17, "女")

# 访问实例属性和方法
print(person1.introduce())
print(person2.introduce())

# 访问类属性和类方法
print(Person.get_species())
print(f"张三是成年人吗: {Person.is_adult(person1.age)}")
print(f"李四是成年人吗: {Person.is_adult(person2.age)}")
print()

# 2. 封装：私有属性和方法
print("=== 封装：私有属性和方法 ===")
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number  # 公有属性
        self.__balance = balance  # 私有属性，双下划线开头
        self._transaction_count = 0  # 受保护属性，单下划线开头
    
    # 公有方法
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transaction_count += 1
            print(f"存款成功，当前余额: {self.__balance}")
        else:
            print("存款金额必须大于0")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_count += 1
            print(f"取款成功，当前余额: {self.__balance}")
        else:
            print("取款金额无效或余额不足")
    
    def get_balance(self):
        return self.__balance
    
    # 私有方法
    def __validate_account(self):
        print("验证账户...")
        return True
    
    def show_account_info(self):
        if self.__validate_account():
            print(f"账户: {self.account_number}, 余额: {self.__balance}, 交易次数: {self._transaction_count}")

# 创建银行账户对象
account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(200)
account.show_account_info()

# 尝试访问私有属性（会报错）
try:
    print(account.__balance)
except AttributeError as e:
    print(f"错误: {e}")

# 通过名称修饰访问私有属性（不推荐）
print(f"通过名称修饰访问私有余额: {account._BankAccount__balance}")
print()

# 3. 继承
print("=== 继承 ===")
# 基类/父类
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"创建了Animal对象: {name}")
    
    def eat(self):
        print(f"{self.name}正在吃东西")
    
    def sleep(self):
        print(f"{self.name}正在睡觉")
    
    def make_sound(self):
        print(f"{self.name}发出声音")

# 派生类/子类
class Dog(Animal):
    def __init__(self, name, breed):
        # 调用父类的初始化方法
        super().__init__(name)
        self.breed = breed
        print(f"创建了Dog对象: {name}, 品种: {breed}")
    
    # 重写父类方法
    def make_sound(self):
        print(f"{self.name}汪汪叫")
    
    # 子类特有方法
    def fetch(self):
        print(f"{self.name}正在捡球")

class Cat(Animal):
    def __init__(self, name, color):
        # 调用父类的初始化方法
        super().__init__(name)
        self.color = color
        print(f"创建了Cat对象: {name}, 颜色: {color}")
    
    # 重写父类方法
    def make_sound(self):
        print(f"{self.name}喵喵叫")
    
    # 子类特有方法
    def climb(self):
        print(f"{self.name}正在爬树")

# 创建子类对象
dog = Dog("旺财", "金毛")
cat = Cat("咪咪", "橘色")

# 调用继承的方法
dog.eat()
cat.sleep()

# 调用重写的方法
dog.make_sound()
cat.make_sound()

# 调用子类特有方法
dog.fetch()
cat.climb()
print()

# 4. 多重继承
print("=== 多重继承 ===")
class Flyable:
    def fly(self):
        print("可以飞行")

class Swimmable:
    def swim(self):
        print("可以游泳")

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name)
        print(f"创建了Duck对象: {name}")
    
    def make_sound(self):
        print(f"{self.name}嘎嘎叫")

# 创建多重继承的对象
duck = Duck("唐老鸭")
duck.make_sound()
duck.fly()
duck.swim()
print()

# 5. 多态
print("=== 多态 ===")
def animal_sound(animal):
    animal.make_sound()

# 不同类型的对象调用相同的方法
animals = [dog, cat, duck]
for animal in animals:
    animal_sound(animal)
print()

# 6. 特殊方法/魔术方法
print("=== 特殊方法/魔术方法 ===")
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # 字符串表示
    def __str__(self):
        return f"《{self.title}》- {self.author}"
    
    # 官方字符串表示
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    # 长度
    def __len__(self):
        return self.pages
    
    # 比较运算符
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False
    
    # 加法运算符
    def __add__(self, other):
        if isinstance(other, Book):
            # 返回一个新的Book对象，合并页数
            return Book(f"{self.title}与{other.title}", "多位作者", self.pages + other.pages)
        return NotImplemented
    
    # 索引访问
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            raise KeyError(f"无效的键: {key}")

# 创建Book对象
book1 = Book("Python编程", "张三", 300)
book2 = Book("Java编程", "李四", 400)
book3 = Book("Python编程", "张三", 300)  # 与book1内容相同

# 使用特殊方法
print(str(book1))  # 调用__str__
print(repr(book1))  # 调用__repr__
print(f"《{book1.title}》有{len(book1)}页")  # 调用__len__
print(f"book1和book3相同吗: {book1 == book3}")  # 调用__eq__

combined_book = book1 + book2  # 调用__add__
print(f"合并后的书: {combined_book}, 总页数: {combined_book.pages}")

# 使用索引访问
print(f"书名: {book1['title']}, 作者: {book1['author']}")
print()

# 7. 属性装饰器
print("=== 属性装饰器 ===")
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    # getter方法
    @property
    def celsius(self):
        return self._celsius
    
    # setter方法
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度(-273.15°C)")
        self._celsius = value
    
    # 只读属性
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    # 只读属性
    @property
    def kelvin(self):
        return self._celsius + 273.15

# 创建Temperature对象
temp = Temperature(25)
print(f"摄氏度: {temp.celsius}°C")
print(f"华氏度: {temp.fahrenheit}°F")
print(f"开尔文: {temp.kelvin}K")

# 修改摄氏度
temp.celsius = 30
print(f"修改后的摄氏度: {temp.celsius}°C")
print(f"对应的华氏度: {temp.fahrenheit}°F")

# 尝试设置无效温度
try:
    temp.celsius = -300
except ValueError as e:
    print(f"错误: {e}")
print()

# 8. 抽象基类
print("=== 抽象基类 ===")
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# 创建形状对象
rectangle = Rectangle(5, 3)
circle = Circle(4)

print(f"矩形面积: {rectangle.area()}, 周长: {rectangle.perimeter()}")
print(f"圆形面积: {circle.area():.2f}, 周长: {circle.perimeter():.2f}")

# 尝试直接实例化抽象类（会报错）
try:
    shape = Shape()
except TypeError as e:
    print(f"错误: {e}")
print()

print("面向对象编程演示完成")



print(__name__)