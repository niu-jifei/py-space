print("-----变量类型注解-----")
"""
变量名: 类型 = 值
"""
num: int = 100
prcie: float = 12.5
message: str = "你好啊"
is_vip: bool = True
result: None = None  # 语法上没有问题，但这么写没有意义


"""
school: str并不是在定义变量，只是说明：如果未来有school变量，那应该是str类型。
Python 执行到school = '尚硅谷'这句代码时，才会真正的定义school变量。
"""
school: str
school = "尚硅谷"

print("*******", school)

print("-----容器类型的注解-----")
# hobby 是列表，并且列表中的所有元素必须是 str 类型
hobby: list[str] = ["抽烟", "喝酒", "烫头"]

# hobby 是列表，并且列表中的元素，可以是：str 或 int 类型
hobby: list[str | int] = ["抽烟", "喝酒", "烫头"]
# 上面这行代码的旧写法如下：
from typing import Union

hobby: list[Union[str, int]] = ["抽烟", "喝酒", "烫头"]

# citys 是集合，并且集合中所有元素必须是 str 类型
citys: set[str] = {"北京", "上海", "深圳"}

# citys 是集合，并且集合中所有元素可以是：str 或 float 或 bool 类型
citys: set[str | float | bool] = {"北京", "上海", "深圳"}

# persons 是字典，键是 str 类型，值是 int 类型
persons: dict[str, int] = {"张三": 18, "李四": 19, "王五": 20}

# persons 是字典，键是 str 或 int 类型，值是 int 类型
persons: dict[str | int, int] = {"张三": 18, "李四": 19, "王五": 20}


print("-----元组的类型注解有些特殊-----")
# scores 是元组，并且元组中仅包含1个int类型的元素
scores: tuple[int] = (60,)

# scores 是元组，并且元组中包含3个int类型的元素
scores: tuple[int, int, int] = (60, 70, 80)

# scores 是元组，并且元组中包含任意个数的元素，但每个元素的类型必须是int
scores: tuple[int, ...] = (60, 70, 80, 90, 100)

# scores 是元组，并且元组中包含任意个数的元素，每个元素的类型可以是：int 或 str
scores: tuple[int | str, ...] = (60, "70", 80, "90", 100)


"""
Python 中存在类型推导：根据变量初始赋值的实际数据，自动推断变量的类型。
1.对于非容器变量：后续如果改变类型，不会警告。
2.对于容器变量：要求内部元素类型必须与推导出来的一致，否则就会警告。
"""
x = 100
x = "尚硅谷"

y = [10, 20, 30]
y.append("40")  # 此行会有警告
print(y)

print("--------函数类型注解---------")
"""
1.函数类型注解：给函数的【参数】和【返回值】添加类型说明。
2.语法格式：函数名(参数1: 类型, 参数2: 类型) -> 返回值类型:
"""


def greet_with_annotation(name: str) -> str:
    """带类型注解的问候函数"""
    return f"你好, {name}!"


# 给参数和返回值加类型注解
def add(x: int, y: int) -> int:
    return x + y


# 带默认值的参数，可以不写注解
def add(x=1, y=1) -> int:
    return x + y


# 设置多个返回值的类型注解
def show_nums_info(nums: list[int]) -> tuple[int, int, float]:
    max_v = max(nums)
    min_v = min(nums)
    return max_v, min_v, max_v / min_v


# 可变参数类型注解
# 设置 *args 的类型注解，要求 args 中的每个参数都必须是 int 类型
def add(*args: int) -> int:
    return sum(args)


# 设置 **kwargs 的类型注解，要求 kwargs 中的每组参数的值，必须是 str 或 int 类型
def show_info(**kwargs: str | int):
    print(kwargs)


# 获取函数的注解信息
print(add.__annotations__)
