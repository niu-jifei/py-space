# 参数类型
print("=== 参数类型 ===")
# 1.位置参数
def describe_person(name, age, job):
    print(f"姓名: {name}, 年龄: {age}, 职业: {job}")

describe_person("张三", 30, "工程师")

# 2.关键字参数
describe_person(name="李四", age=25, job="设计师")
describe_person(job="教师", name="王五", age=28)  # 顺序可以不同

# 3.默认参数
def introduce(name, age, city="北京"):
    print(f"我叫{name}，今年{age}岁，来自{city}")

introduce("赵六", 35)  # 使用默认城市
introduce("钱七", 40, "上海")  # 覆盖默认城市
print()

# 4.1 仅限位置参数 (/)
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

# 4.2 仅限关键字参数 (*)
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

# 4.3 组合使用 / 和 *
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

# 5. 可变参数
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


# 6. 参数解包
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


# 7. None
# None是一个特殊的字面量，它表示：空值 / 无值 / 无意义。
msg = None

# None 的类型是 NoneType。
print(type(msg))

# None 转为布尔值是 False。
print(bool(msg))
if not msg:
    print('你好')

# 不能参与数学运算，也不能与字符串拼接。
# result1 = msg + 1
# result1 = msg + 'hello'
