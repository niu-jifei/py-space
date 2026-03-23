"""
概念：用一条简洁语句，从可迭代对象中，生成新列表的语法结构。
语法格式：[ 表达式 for 变量 in 可迭代对象 ]
"""

# 需求：让nums列表中所有的元素，都变为原来的2倍

# 方式一：用map函数
nums = [10, 20, 30, 40]
result = list(map(lambda n: n * 2, nums))
print(result)

# 方式二：使用for循环结合append方法
nums = [10, 20, 30, 40]
result = []
for n in nums:
    result.append(n * 2)
print(result)

# 方式三：使用列表推导式(列表推导式就是上面 for + append 的简写形式)
nums = [10, 20, 30, 40]
result = [n * 2 for n in nums]
print(result)

# 带条件的列表推导式
nums = [10, 20, 30, 40]
result = [n * 2 for n in nums if n > 20]
print(result)

# 字典推导式
names = ["张三", "李四", "王五"]
scores = [60, 70, 80]
result = {names[i]: scores[i] for i in range(len(names))}
print(result)

# 集合推导式
names = ["张三", "李四", "王五"]
result = {n + "！" for n in names}
print(result)

names = ["张三", "李四", "王五"]
# 注意：Python中没有元组推导式，下面这种写法叫：生成器（后面会仔细讲）
result = (n + "?" for n in names)
print(list(result))
print(tuple(result))
print(result)
