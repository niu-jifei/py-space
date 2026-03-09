# 案例演示：Python 函数用法

# 1. 基本函数定义和调用
print("=== 基本函数定义和调用 ===")
def greet():
    """这是一个简单的问候函数"""
    print("你好，世界！")

# 调用函数
greet()

# 带参数的函数
def greet_person(name):
    """向指定的人问好"""
    print(f"你好，{name}！")

# 调用带参数的函数
greet_person("小明")
greet_person("小红")
print()

# 2. 函数返回值
print("=== 函数返回值 ===")
def add(a, b):
    """两个数相加并返回结果"""
    return a + b

# 调用函数并使用返回值
result = add(5, 3)
print(f"5 + 3 = {result}")

# 多个返回值
def calculate(a, b):
    """返回两个数的和、差、积、商"""
    return a + b, a - b, a * b, a / b

# 接收多个返回值
sum_result, diff_result, product_result, quotient_result = calculate(10, 2)
print(f"10 + 2 = {sum_result}")
print(f"10 - 2 = {diff_result}")
print(f"10 * 2 = {product_result}")
print(f"10 / 2 = {quotient_result}")
print()

# 3. 参数类型
print("=== 参数类型 ===")
# 位置参数
def describe_person(name, age, job):
    print(f"姓名: {name}, 年龄: {age}, 职业: {job}")

describe_person("张三", 30, "工程师")

# 关键字参数
describe_person(name="李四", age=25, job="设计师")
describe_person(job="教师", name="王五", age=28)  # 顺序可以不同

# 默认参数
def introduce(name, age, city="北京"):
    print(f"我叫{name}，今年{age}岁，来自{city}")

introduce("赵六", 35)  # 使用默认城市
introduce("钱七", 40, "上海")  # 覆盖默认城市
print()

# 3.1 仅限位置参数 (/)
print("=== 仅限位置参数 (/) ===")
# 使用 / 分隔符定义仅限位置参数
# / 前面的参数只能通过位置传递，不能使用关键字
def position_only_func(a, b, /, c):
    """a和b是仅限位置参数，c可以是位置或关键字参数"""
    print(f"a = {a}, b = {b}, c = {c}")

# 正确调用方式
position_only_func(1, 2, 3)  # 全部使用位置参数
position_only_func(1, 2, c=3)  # c使用关键字参数

# 错误调用方式（会报错）
try:
    position_only_func(a=1, b=2, c=3)  # a和b不能使用关键字参数
except TypeError as e:
    print(f"错误: {e}")

# 所有参数都是仅限位置参数
def all_position_only(a, b, c, /):
    print(f"a = {a}, b = {b}, c = {c}")

all_position_only(10, 20, 30)  # 正确

try:
    all_position_only(10, 20, c=30)  # 错误，所有参数都必须是位置参数
except TypeError as e:
    print(f"错误: {e}")
print()

# 3.2 仅限关键字参数 (*)
print("=== 仅限关键字参数 (*) ===")
# 使用 * 分隔符定义仅限关键字参数
# * 后面的参数只能通过关键字传递，不能使用位置
def keyword_only_func(a, b, *, c, d):
    """a和b可以是位置或关键字参数，c和d是仅限关键字参数"""
    print(f"a = {a}, b = {b}, c = {c}, d = {d}")

# 正确调用方式
keyword_only_func(1, 2, c=3, d=4)  # a和b使用位置参数，c和d使用关键字参数
keyword_only_func(a=1, b=2, c=3, d=4)  # 全部使用关键字参数

# 错误调用方式（会报错）
try:
    keyword_only_func(1, 2, 3, 4)  # c和d不能使用位置参数
except TypeError as e:
    print(f"错误: {e}")

# 所有参数都是仅限关键字参数
def all_keyword_only(*, a, b, c):
    print(f"a = {a}, b = {b}, c = {c}")

all_keyword_only(a=10, b=20, c=30)  # 正确

try:
    all_keyword_only(10, 20, 30)  # 错误，所有参数都必须是关键字参数
except TypeError as e:
    print(f"错误: {e}")
print()

# 3.3 组合使用 / 和 *
print("=== 组合使用 / 和 * ===")
# 同时使用 / 和 * 定义不同类型的参数
def mixed_params(a, b, /, c, d, *, e, f):
    """
    a, b: 仅限位置参数
    c, d: 位置或关键字参数
    e, f: 仅限关键字参数
    """
    print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, f = {f}")

# 正确调用方式
mixed_params(1, 2, 3, 4, e=5, f=6)  # a,b位置；c,d位置；e,f关键字
mixed_params(1, 2, c=3, d=4, e=5, f=6)  # a,b位置；c,d关键字；e,f关键字

# 错误调用方式（会报错）
try:
    mixed_params(a=1, b=2, c=3, d=4, e=5, f=6)  # a,b不能使用关键字参数
except TypeError as e:
    print(f"错误: {e}")

try:
    mixed_params(1, 2, 3, 4, 5, 6)  # e,f不能使用位置参数
except TypeError as e:
    print(f"错误: {e}")
print()

# 3.4 实际应用示例
print("=== 实际应用示例 ===")
# 计算器示例：使用仅限位置参数确保数值参数必须按位置传递
def calculator(a, b, /, operation="add", *, precision=2):
    """
    计算器函数
    a, b: 仅限位置参数（必须按位置传递的数值）
    operation: 位置或关键字参数（运算类型）
    precision: 仅限关键字参数（结果精度）
    """
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        result = a / b
    else:
        raise ValueError(f"不支持的运算: {operation}")
    
    return round(result, precision)

# 正确调用方式
print(f"加法: {calculator(10, 5)}")  # 使用默认运算和精度
print(f"减法: {calculator(10, 5, 'subtract')}" )  # 指定运算
print(f"乘法: {calculator(10, 5, 'multiply', precision=0)}")  # 指定精度
print(f"除法: {calculator(10, 5, operation='divide', precision=3)}")  # 使用关键字参数

# 错误调用方式（会报错）
try:
    calculator(a=10, b=5)  # a,b不能使用关键字参数
except TypeError as e:
    print(f"错误: {e}")

try:
    calculator(10, 5, 'add', 2)  # precision不能使用位置参数
except TypeError as e:
    print(f"错误: {e}")
print()

# 4. 可变参数
print("=== 可变参数 ===")
# *args - 任意数量的位置参数
def sum_all(*numbers):
    """计算所有数字的和"""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"1 + 2 + 3 + 4 + 5 = {sum_all(1, 2, 3, 4, 5)}")
print(f"10 + 20 + 30 = {sum_all(10, 20, 30)}")

# **kwargs - 任意数量的关键字参数
def print_info(**info):
    """打印所有信息"""
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="周八", age=32, city="广州", hobby="编程")

# 混合使用普通参数、*args和**kwargs
def complex_function(required, default="默认值", *args, **kwargs):
    print(f"必需参数: {required}")
    print(f"默认参数: {default}")
    print(f"额外位置参数: {args}")
    print(f"额外关键字参数: {kwargs}")

complex_function("必需", "自定义", 1, 2, 3, extra1="值1", extra2="值2")
print()

# 5. 参数解包
print("=== 参数解包 ===")
# 列表/元组解包为位置参数
def multiply(a, b, c):
    return a * b * c

numbers = [2, 3, 4]
print(f"2 * 3 * 4 = {multiply(*numbers)}")

# 字典解包为关键字参数
def create_profile(name, age, city):
    return f"姓名: {name}, 年龄: {age}, 城市: {city}"

profile_data = {"name": "吴九", "age": 27, "city": "深圳"}
print(create_profile(**profile_data))
print()

# 6. 函数作用域
print("=== 函数作用域 ===")
global_var = "全局变量"

def scope_demo():
    local_var = "局部变量"
    print(f"函数内部访问全局变量: {global_var}")
    print(f"函数内部访问局部变量: {local_var}")
    
    # 修改全局变量需要使用global关键字
    global global_var
    global_var = "修改后的全局变量"
    print(f"修改后的全局变量: {global_var}")

scope_demo()
print(f"函数外部访问全局变量: {global_var}")

# 嵌套函数和闭包
def outer_function(x):
    """
    外部函数：用于创建闭包

    :param x： 外部函数的参数
    :return : 内部函数
    
    """
    def inner_function(y):
        """
        内部函数：使用了外部函数的变量x

        param y: 内部函数的参数
        return : 两个数的和
        
        """
        return x + y  # 访问外部函数的变量
    
    return inner_function  # 返回内部函数

# 创建闭包
add_five = outer_function(5)
print(f"5 + 10 = {add_five(10)}")
print(f"5 + 20 = {add_five(20)}")
print()

# 7. 递归函数
print("=== 递归函数 ===")
# 阶递归计算阶乘
def factorial(n):
    """递归计算阶乘"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

for i in range(1, 6):
    print(f"{i}! = {factorial(i)}")

# 递归计算斐波那契数列
def fibonacci(n):
    """递归计算斐波那契数列"""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("斐波那契数列前10项:")
fib_sequence = [fibonacci(i) for i in range(10)]
print(fib_sequence)
print()

# 8. 装饰器
print("=== 装饰器 ===")
# 简单装饰器
def simple_decorator(func):
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    return wrapper

@simple_decorator
def say_hello():
    print("你好!")

say_hello()

# 带参数的装饰器
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet_repeat(name):
    print(f"你好, {name}!")

greet_repeat("小明")

# 保留原函数信息的装饰器
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数 {func.__name__} 执行时间: {end_time - start_time:.4f}秒")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(0.1)
    return "执行完成"

print(slow_function())
print(f"函数名: {slow_function.__name__}")  # 保留了原函数名
print()

# 9. 高阶函数
print("=== 高阶函数 ===")
# 函数作为参数
def apply_operation(func, x, y):
    return func(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print(f"加法: {apply_operation(add, 5, 3)}")
print(f"乘法: {apply_operation(multiply, 5, 3)}")

# 函数作为返回值
def get_operation(operation):
    if operation == "add":
        return add
    elif operation == "multiply":
        return multiply
    else:
        return lambda x, y: x - y  # 返回匿名函数

add_func = get_operation("add")
sub_func = get_operation("subtract")
print(f"加法: {add_func(10, 5)}")
print(f"减法: {sub_func(10, 5)}")
print()

# 10. 匿名函数 (lambda)
print("=== 匿名函数 (lambda) ===")
# 基本lambda表达式
square = lambda x: x ** 2
print(f"5的平方: {square(5)}")

# 带多个参数的lambda
add_lambda = lambda x, y: x + y
print(f"3 + 7 = {add_lambda(3, 7)}")

# 在高阶函数中使用lambda
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"原列表: {numbers}")
print(f"平方列表: {squared_numbers}")

# 使用lambda进行条件过滤
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数列表: {even_numbers}")

# 使用lambda进行排序
people = [{"name": "张三", "age": 30}, {"name": "李四", "age": 25}, {"name": "王五", "age": 35}]
sorted_people = sorted(people, key=lambda person: person["age"])
print("按年龄排序:")
for person in sorted_people:
    print(f"{person['name']}: {person['age']}岁")
print()

# 11. 生成器函数
print("=== 生成器函数 ===")
# 基本生成器函数
def count_up_to(n):
    """生成从1到n的数字"""
    i = 1
    while i <= n:
        yield i
        i += 1

print("计数到5:")
for num in count_up_to(5):
    print(num, end=" ")
print()

# 斐波那契数列生成器
def fibonacci_generator(n):
    """生成斐波那契数列的前n项"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("斐波那契数列前10项:")
fib_gen = fibonacci_generator(10)
for num in fib_gen:
    print(num, end=" ")
print()

# 生成器表达式
squares_gen = (x ** 2 for x in range(10))
print("平方数生成器:")
for i, square in enumerate(squares_gen):
    if i < 5:  # 只打印前5个
        print(f"{i} 的平方: {square}")
    else:
        break
print()

# 12. 函数注解
print("=== 函数注解 ===")
# 带类型注解的函数
def greet_with_annotation(name: str) -> str:
    """带类型注解的问候函数"""
    return f"你好, {name}!"

print(greet_with_annotation("小明"))

# 复杂类型注解
from typing import List, Dict, Union, Optional

def process_data(data: List[Dict[str, Union[str, int]]]) -> Optional[str]:
    """处理数据的函数"""
    if not data:
        return None
    
    result = "处理结果:\n"
    for item in data:
        name = item.get("name", "未知")
        age = item.get("age", 0)
        result += f"姓名: {name}, 年龄: {age}\n"
    
    return result

sample_data = [
    {"name": "张三", "age": 30},
    {"name": "李四", "age": 25}
]

print(process_data(sample_data))
print()

# 13. 内置函数应用示例
print("=== 内置函数应用示例 ===")
# map函数
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"原列表: {numbers}")
print(f"平方列表: {squared}")

# filter函数
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数列表: {evens}")

# reduce函数
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"列表元素乘积: {product}")

# zip函数
names = ["张三", "李四", "王五"]
ages = [30, 25, 35]
cities = ["北京", "上海", "广州"]
combined = list(zip(names, ages, cities))
print("组合数据:")
for name, age, city in combined:
    print(f"姓名: {name}, 年龄: {age}, 城市: {city}")

# enumerate函数
print("使用enumerate:")
for index, name in enumerate(names):
    print(f"索引 {index}: {name}")
print()

# 14. 函数式编程示例
print("=== 函数式编程示例 ===")
# 使用map和filter组合
numbers = list(range(1, 21))
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 1, numbers)))
print(f"1-20中奇数的平方: {result}")

# 使用列表推导式替代map和filter
result_comp = [x ** 2 for x in numbers if x % 2 == 1]
print(f"使用列表推导式: {result_comp}")

# 使用functools.partial创建偏函数
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(f"5的平方: {square(5)}")
print(f"5的立方: {cube(5)}")
print()

# 15. 函数设计最佳实践
print("=== 函数设计最佳实践 ===")
# 单一职责原则
def is_even(n):
    """判断一个数是否为偶数"""
    return n % 2 == 0

def filter_even_numbers(numbers):
    """过滤出偶数"""
    return [num for num in numbers if is_even(num)]

numbers = list(range(1, 11))
evens = filter_even_numbers(numbers)
print(f"原列表: {numbers}")
print(f"偶数列表: {evens}")

# 使用默认参数避免None检查
def process_items(items=None):
    """处理项目列表"""
    if items is None:
        items = []
    # 处理逻辑
    return [item.upper() for item in items]

print(process_items(["apple", "banana"]))
print(process_items())  # 使用空列表

# 使用*args和**kwargs提高灵活性
def flexible_function(*args, **kwargs):
    """灵活的函数示例"""
    print("位置参数:", args)
    print("关键字参数:", kwargs)

flexible_function(1, 2, 3, name="张三", age=30)
print()