"""
数据处理函数
"""

"""

map函数：对一组数据中的每一个元素，统一执行某种操作（加工），并生成一组新数据。
语法格式：map(操作函数, 可迭代对象)
"""
print("------------map------------")
# 统一数据处理
nums = [10, 20, 30, 40]
# map函数的返回值是一个迭代器对象，需要我们自己去手动遍历，或者手动类型转换
result = map(lambda x: x * 2, nums)
print(list(result))
print(nums)

# 字符串转换
names = ("python", "java", "js")
result = map(lambda x: x.upper(), names)
print(tuple(result))
print(names)

# 类型转换
str_number = {"1", "2", "3"}
result = map(int, str_number)
print(set(result))
print(str_number)

# 注意点：
# 1.延迟执行：map 不会立刻计算，只有在“需要结果”时才执行计算。
# 2.返回的是迭代器对象，且一旦遍历完成，就会被“耗尽”。
# 3.map不会影响元素数量。

nums = [10, 20, 30, 40]
result = list(map(lambda x: x * 2, nums))
print(result)
print(result)
print(result)
print(result)


"""
filter函数：从一组数据中，筛选出符合条件的元素（过滤），并组成一组新数据。
语法格式：filter(过滤函数, 可迭代对象)
"""
print("------------filter------------")
# 筛选数值
nums = [10, 20, 30, 40, 50]
result = filter(lambda n: n > 30, nums)
print(list(result))
print(nums)

# 筛选成年人
persons = [
    {"name": "张三", "age": 15, "gender": "男"},
    {"name": "李四", "age": 16, "gender": "女"},
    {"name": "王五", "age": 17, "gender": "男"},
    {"name": "李华", "age": 18, "gender": "女"},
    {"name": "赵六", "age": 19, "gender": "女"},
    {"name": "孙七", "age": 20, "gender": "男"},
]
result = filter(lambda p: p["age"] >= 18, persons)
print(list(result))

# 过滤一下非法字符串
names = ["张三", "", "李四", None, "王五"]
result = filter(lambda n: n, names)
print(list(result))

# 注意点
# 1.延迟执行：filter不会立刻筛选，只有在“需要结果”时才执行。
# 2.返回的是迭代器对象，且一旦遍历完成就会被“耗尽”。
# 3.filter可能会影响元素数量。

# filter函数的特殊用法：如果不传递过滤函数，那么自动会过滤掉“假值”
data = [0, 1, "", "hello", [], (), 5]
result = filter(None, data)
print(list(result))


print("------------sorted------------")
"""
sorted函数：对一组数据进行排序，返回一组新数据。
语法格式：sorted(可迭代对象, key=xxx, reverse=xxx)
"""
# 数字排序
nums = [30, 40, 20, 10]
result = sorted(nums, reverse=True)
# result = sorted(nums)
print(result)

# 按照字符串的长度去排序
names = ["python", "sql", "java"]
result = sorted(names, key=len, reverse=True)
print(result)

# 根据字典中的某个字段进行排序
persons = [
    {"name": "张三", "age": 15, "gender": "男"},
    {"name": "李四", "age": 17, "gender": "女"},
    {"name": "王五", "age": 19, "gender": "男"},
    {"name": "李华", "age": 20, "gender": "女"},
    {"name": "赵六", "age": 18, "gender": "女"},
    {"name": "孙七", "age": 16, "gender": "男"},
]
result = sorted(persons, key=lambda p: p["age"], reverse=True)
print(result)

# 我们之前讲的max函数、min函数，也可以传递key参数，用于设置筛选依据
result1 = max(persons, key=lambda p: p["age"])
result2 = min(persons, key=lambda p: p["age"])
print(result1)
print(result2)

print("------------reduce------------")
"""
reduce函数：将一组数据不断“合并”，最终归并成一个结果。
语法格式：reduce(合并函数, 可迭代对象, 初始值)。

    
备注：reduce函数需要从functools模块中引入才能使用。
"""
# 从 functools 模块中引入 reduce
from functools import reduce

# 数值统计
nums = [1, 2, 3, 4, 5]
result = reduce(lambda a, b: a + b, nums, 10)
print(result)

# 字符串拼接
str_list = ["ab", "cd", "ef"]
result = reduce(lambda a, b: a + b, str_list)
print(result)
