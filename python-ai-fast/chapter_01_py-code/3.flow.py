# 案例演示：Python 的所有流程控制语句

# 1. if 条件语句
print("=== if 条件语句 ===")
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 三元表达式
age = 20
status = "成年" if age >= 18 else "未成年"
print(f"年龄: {age}, 状态: {status}")
print()

# 2. for 循环
print("=== for 循环 ===")
# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"水果: {fruit}")

# 使用 range()
print("使用 range():")
for i in range(5):
    print(f"i = {i}")

# 使用 enumerate() 获取索引和值
print("使用 enumerate():")
for index, fruit in enumerate(fruits):
    print(f"索引 {index}: {fruit}")

# 使用 zip() 遍历多个序列
print("使用 zip():")
names = ["张三", "李四", "王五"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"姓名: {name}, 年龄: {age}")
print()

# 3. while 循环
print("=== while 循环 ===")
count = 0
while count < 5:
    print(f"count = {count}")
    count += 1

# 使用 break 和 continue
print("使用 break 和 continue:")
num = 0
while num < 10:
    num += 1
    if num == 3:
        continue  # 跳过3
    if num == 7:
        break  # 在7处停止
    print(f"num = {num}")
print()

# 4. 嵌套循环
print("=== 嵌套循环 ===")
# 九九乘法表
print("九九乘法表:")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} × {i} = {i * j}", end="\t")
    print()  # 换行
print()

# 5. 列表推导式
print("=== 列表推导式 ===")
# 基本列表推导式
squares = [x ** 2 for x in range(10)]
print(f"平方数列表: {squares}")

# 带条件的列表推导式
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(f"偶数的平方: {even_squares}")

# 嵌套列表推导式
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"矩阵: {matrix}")
print()

# 6. 字典推导式
print("=== 字典推导式 ===")
# 基本字典推导式
word = "hello"
char_count = {char: word.count(char) for char in set(word)}
print(f"字符计数: {char_count}")

# 带条件的字典推导式
squares_dict = {x: x ** 2 for x in range(10) if x % 2 == 0}
print(f"偶数的平方字典: {squares_dict}")
print()

# 7. 集合推导式
print("=== 集合推导式 ===")
# 基本集合推导式
unique_squares = {x ** 2 for x in range(10)}
print(f"唯一的平方数集合: {unique_squares}")

# 带条件的集合推导式
even_squares_set = {x ** 2 for x in range(10) if x % 2 == 0}
print(f"偶数的平方集合: {even_squares_set}")
print()

# 8. 生成器表达式
print("=== 生成器表达式 ===")
# 基本生成器表达式
squares_gen = (x ** 2 for x in range(10))
print("生成器表达式:")
for i, square in enumerate(squares_gen):
    if i < 5:  # 只打印前5个
        print(f"{i} 的平方: {square}")
    else:
        break

# 带条件的生成器表达式
even_squares_gen = (x ** 2 for x in range(10) if x % 2 == 0)
print("偶数的平方生成器:")
for square in even_squares_gen:
    print(f"偶数平方: {square}")
print()

# 9. try-except 异常处理
print("=== try-except 异常处理 ===")
# 基本异常处理
try:
    result = 10 / 0
except ZeroDivisionError:
    print("捕获到除零错误")

# 多种异常处理
try:
    num = int("abc")
except ValueError:
    print("捕获到值错误")
except Exception as e:
    print(f"捕获到其他异常: {e}")
else:
    print("没有异常发生")
finally:
    print("无论如何都会执行")
print()

# 10. 函数定义与调用
print("=== 函数定义与调用 ===")
# 基本函数
def greet(name):
    return f"你好, {name}!"

print(greet("小明"))

# 带默认参数的函数
def power(base, exponent=2):
    return base ** exponent

print(f"2的平方: {power(2)}")
print(f"2的3次方: {power(2, 3)}")

# 可变参数函数
def sum_all(*args):
    return sum(args)

print(f"1+2+3+4+5 = {sum_all(1, 2, 3, 4, 5)}")

# 关键字参数函数
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="张三", age=25, city="北京")
print()

# 11. 递归函数
print("=== 递归函数 ===")
# 阶乘函数
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

for i in range(1, 6):
    print(f"{i}! = {factorial(i)}")

# 斐波那契数列
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("斐波那契数列前10项:")
fib_sequence = [fibonacci(i) for i in range(10)]
print(fib_sequence)
print()

# 12. 装饰器
print("=== 装饰器 ===")
# 计时装饰器
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数 {func.__name__} 执行时间: {end_time - start_time:.4f}秒")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "执行完成"

print(slow_function())

# 日志装饰器
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"函数 {func.__name__} 执行完毕")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

print(f"3 + 5 = {add(3, 5)}")
print()

# 13. 上下文管理器
print("=== 上下文管理器 ===")
# 使用 with 语句处理文件
try:
    # 创建一个临时文件并写入内容
    with open("temp.txt", "w", encoding="utf-8") as f:
        f.write("这是一个临时文件\n")
        f.write("用于演示上下文管理器\n")
    
    # 读取文件内容
    with open("temp.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print("文件内容:")
        print(content)
except FileNotFoundError:
    print("文件不存在")
except Exception as e:
    print(f"发生错误: {e}")
print()

# 14. 迭代器
print("=== 迭代器 ===")
# 自定义迭代器
class Countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        else:
            self.start -= 1
            return self.start + 1

print("倒计时:")
for i in Countdown(5):
    print(i)
print()

# 15. 生成器函数
print("=== 生成器函数 ===")
# 基本生成器函数
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

print("计数到5:")
for num in count_up_to(5):
    print(num)

# 斐波那契数列生成器
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("斐波那契数列前10项:")
fib_gen = fibonacci_generator(10)
for num in fib_gen:
    print(num, end=" ")
print()