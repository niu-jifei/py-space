# 案例演示： Python的数据结构， 列表 List，元祖 Tuple， 集合 Set， 字典 Dict

# 1. 列表 (List)
print("=== 列表 (List) ===")
# 创建列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print(f"水果列表: {fruits}")
print(f"数字列表: {numbers}")
print(f"混合列表: {mixed}")

# 列表基本操作
print("\n列表基本操作:")
print(f"列表长度: {len(fruits)}")
print(f"第一个元素: {fruits[0]}")
print(f"最后一个元素: {fruits[-1]}")
print(f"切片 [1:3]: {fruits[1:3]}")

# 列表修改
print("\n列表修改:")
fruits[0] = "草莓"  # 修改元素
print(f"修改后: {fruits}")

fruits.append("西瓜")  # 添加元素到末尾
print(f"添加西瓜后: {fruits}")

fruits.insert(1, "芒果")  # 在指定位置插入元素
print(f"在位置1插入芒果: {fruits}")

removed = fruits.pop()  # 移除并返回最后一个元素
print(f"移除的元素: {removed}, 移除后: {fruits}")

fruits.remove("香蕉")  # 移除指定元素
print(f"移除香蕉后: {fruits}")

# 列表排序
print("\n列表排序:")
numbers.sort()
print(f"升序排序: {numbers}")

numbers.sort(reverse=True)
print(f"降序排序: {numbers}")

# 列表推导式
print("\n列表推导式:")
squares = [x ** 2 for x in range(10)]
print(f"0-9的平方: {squares}")

even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(f"0-9中偶数的平方: {even_squares}")

# 列表常用方法
print("\n列表常用方法:")
print(f"'苹果'是否在列表中: {'苹果' in fruits}")
print(f"'香蕉'是否在列表中: {'香蕉' in fruits}")
print(f"'苹果'在列表中的索引: {fruits.index('苹果') if '苹果' in fruits else '不存在'}")
print(f"'苹果'出现的次数: {fruits.count('苹果') if '苹果' in fruits else 0}")

# 列表复制
print("\n列表复制:")
fruits_copy = fruits.copy()  # 浅拷贝
print(f"复制列表: {fruits_copy}")
fruits_copy.append("柠檬")
print(f"修改复制列表后原列表: {fruits}")
print(f"修改复制列表后复制列表: {fruits_copy}")
print()

# 2. 元组 (Tuple)
print("=== 元组 (Tuple) ===")
# 创建元组
empty_tuple = ()
single_item_tuple = (1,)  # 注意逗号，否则会被当作表达式
coordinates = (10, 20, "a")
mixed_tuple = (1, "hello", 3.14, True)

print(f"空元组: {empty_tuple}")
print(f"单项元组: {single_item_tuple}")
print(f"坐标元组: {coordinates}")
print(f"混合元组: {mixed_tuple}")

# 元组基本操作
print("\n元组基本操作:")
print(f"元组长度: {len(coordinates)}")
print(f"第一个元素: {coordinates[0]}")
print(f"最后一个元素: {coordinates[-1]}")
print(f"切片 [0:1]: {coordinates[0:1]}")

# 元组不可变性
print("\n元组不可变性:")
try:
    coordinates[0] = 15  # 尝试修改元组元素
except TypeError as e:
    print(f"错误: {e}")

# 元组解包
print("\n元组解包:")
x, y, a = coordinates
print(f"解包后: x = {x}, y = {y}, a = {a}, {type(a)}")

# 元组常用方法
print("\n元组常用方法:")
print(f"'hello'是否在元组中: {'hello' in mixed_tuple}")
print(f"1在元组中的索引: {mixed_tuple.index(1)}")
print(f"1在元组中出现的次数: {mixed_tuple.count(1)}")

# 元组与列表转换
print("\n元组与列表转换:")
tuple_to_list = list(coordinates)
print(f"元组转列表: {tuple_to_list}")

list_to_tuple = tuple(fruits)
print(f"列表转元组: {list_to_tuple}")
print()

# 3. 集合 (Set)
print("=== 集合 (Set) ===")
# 创建集合
empty_set = set()
numbers_set = {1, 2, 3, 4, 5}
fruits_set = {"苹果", "香蕉", "橙子", "苹果"}  # 重复元素会被自动去除

print(f"空集合: {empty_set}")
print(f"数字集合: {numbers_set}")
print(f"水果集合: {fruits_set}")  # 注意"苹果"只出现一次

# 集合基本操作
print("\n集合基本操作:")
print(f"集合长度: {len(fruits_set)}")
print(f"'苹果'是否在集合中: {'苹果' in fruits_set}")
print(f"'西瓜'是否在集合中: {'西瓜' in fruits_set}")

# 集合修改
print("\n集合修改:")
fruits_set.add("西瓜")  # 添加元素
print(f"添加西瓜后: {fruits_set}")

fruits_set.remove("香蕉")  # 移除元素，如果元素不存在会报错
print(f"移除香蕉后: {fruits_set}")

fruits_set.discard("柠檬")  # 移除元素，如果元素不存在不会报错
print(f"尝试移除柠檬后: {fruits_set}")

removed = fruits_set.pop()  # 移除并返回一个随机元素
print(f"随机移除的元素: {removed}, 移除后: {fruits_set}")

# 集合运算
print("\n集合运算:")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"集合1: {set1}")
print(f"集合2: {set2}")
print(f"并集: {set1.union(set2)} 或 {set1 | set2}")
print(f"交集: {set1.intersection(set2)} 或 {set1 & set2}")
print(f"差集: {set1.difference(set2)} 或 {set1 - set2}")
print(f"对称差集: {set1.symmetric_difference(set2)} 或 {set1 ^ set2}")

# 集合推导式
print("\n集合推导式:")
squares_set = {x ** 2 for x in range(10)}
print(f"0-9的平方集合: {squares_set}")

even_squares_set = {x ** 2 for x in range(10) if x % 2 == 0}
print(f"0-9中偶数的平方集合: {even_squares_set}")
print()

# 4. 字典 (Dict)
print("=== 字典 (Dict) ===")
# 创建字典
empty_dict = {}
student = {"name": "张三", "age": 20, "major": "计算机科学"}
numbers_dict = {1: "one", 2: "two", 3: "three"}

print(f"空字典: {empty_dict}")
print(f"学生字典: {student}")
print(f"数字字典: {numbers_dict}")

# 字典基本操作
print("\n字典基本操作:")
print(f"字典长度: {len(student)}")
print(f"姓名: {student['name']}")
print(f"年龄: {student['age']}")

# 使用get方法安全访问
print(f"专业: {student.get('major')}")
print(f"班级: {student.get('class', '未知')}")  # 提供默认值

# 字典修改
print("\n字典修改:")
student["age"] = 21  # 修改现有键值
print(f"修改年龄后: {student}")

student["class"] = "计算机1班"  # 添加新键值
print(f"添加班级后: {student}")

removed_value = student.pop("major")  # 移除并返回指定键的值
print(f"移除的专业: {removed_value}, 移除后: {student}")

last_item = student.popitem()  # 移除并返回最后一对键值
print(f"移除的键值对: {last_item}, 移除后: {student}")

# 字典遍历
print("\n字典遍历:")
student = {"name": "李四", "age": 22, "major": "数学", "class": "数学1班"}

print("遍历键:")
for key in student.keys():
    print(f"  {key}")

print("遍历值:")
for value in student.values():
    print(f"  {value}")

print("遍历键值对:")
for key, value in student.items():
    print(f"  {key}: {value}")

# 字典常用方法
print("\n字典常用方法:")
print(f"'name'是否在字典中: {'name' in student}")
print(f"'gender'是否在字典中: {'gender' in student}")

# 字典推导式
print("\n字典推导式:")
square_dict = {x: x ** 2 for x in range(5)}
print(f"0-4的平方字典: {square_dict}")

# 字典合并
print("\n字典合并:")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Python 3.9+ 使用 | 运算符合并
try:
    merged_dict = dict1 | dict2
    print(f"使用 | 合并: {merged_dict}")
except:
    print("当前Python版本不支持 | 运算符")

# 使用update方法合并
dict1_copy = dict1.copy()
dict1_copy.update(dict2)
print(f"使用update合并: {dict1_copy}")

# 使用**解包合并
merged_dict = {**dict1, **dict2}
print(f"使用**解包合并: {merged_dict}")
print()

# 5. 数据结构比较与应用场景
print("=== 数据结构比较与应用场景 ===")
# 创建相同的数据但使用不同数据结构
data_list = [1, 2, 3, 4, 5]
data_tuple = (1, 2, 3, 4, 5)
data_set = {1, 2, 3, 4, 5}
data_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

print(f"列表: {data_list}")
print(f"元组: {data_tuple}")
print(f"集合: {data_set}")
print(f"字典: {data_dict}")

# 性能比较示例
import time

# 测试访问速度
test_data = list(range(100000))
test_tuple = tuple(range(100000))

# 列表访问时间
start_time = time.time()
for i in range(1000):
    _ = test_data[i * 100]
list_access_time = time.time() - start_time

# 元组访问时间
start_time = time.time()
for i in range(1000):
    _ = test_tuple[i * 100]
tuple_access_time = time.time() - start_time

print(f"\n访问速度比较:")
print(f"列表访问时间: {list_access_time:.6f}秒")
print(f"元组访问时间: {tuple_access_time:.6f}秒")

# 测试成员检查速度
test_list = list(range(10000))
test_set = set(range(10000))

# 列表成员检查时间
start_time = time.time()
for i in range(1000):
    _ = i * 10 in test_list
list_check_time = time.time() - start_time

# 集合成员检查时间
start_time = time.time()
for i in range(1000):
    _ = i * 10 in test_set
set_check_time = time.time() - start_time

print(f"\n成员检查速度比较:")
print(f"列表成员检查时间: {list_check_time:.6f}秒")
print(f"集合成员检查时间: {set_check_time:.6f}秒")

# 应用场景示例
print("\n应用场景示例:")
print("1. 列表 - 适合存储需要修改的有序数据，如购物车")
cart = ["苹果", "香蕉", "橙子"]
cart.append("葡萄")
print(f"购物车: {cart}")

print("\n2. 元组 - 适合存储不需要修改的有序数据，如坐标")
point = (10, 20)
x, y = point
print(f"坐标: ({x}, {y})")

print("\n3. 集合 - 适合存储唯一值和快速成员检查，如标签")
tags = {"python", "编程", "数据科学", "人工智能"}
tags.add("机器学习")
print(f"标签: {tags}")
print(f"'python'是否在标签中: {'python' in tags}")

print("\n4. 字典 - 适合存储键值对数据，如用户信息")
user = {
    "username": "zhangsan",
    "email": "zhangsan@example.com",
    "age": 25,
    "is_active": True
}
print(f"用户信息: {user}")
print(f"用户名: {user['username']}")
print(f"邮箱: {user['email']}")

# 嵌套数据结构
print("\n嵌套数据结构示例:")
students = [
    {"name": "张三", "scores": {"math": 90, "english": 85, "science": 92}},
    {"name": "李四", "scores": {"math": 85, "english": 90, "science": 88}},
    {"name": "王五", "scores": {"math": 92, "english": 88, "science": 95}}
]

print("学生成绩:")
for student in students:
    name = student["name"]
    scores = student["scores"]
    avg_score = sum(scores.values()) / len(scores)
    print(f"{name}: 平均分 {avg_score:.2f}")

# 复杂数据结构操作
print("\n复杂数据结构操作:")
# 找出数学成绩最高的学生
math_scores = [(student["name"], student["scores"]["math"]) for student in students]
top_math_student = max(math_scores, key=lambda x: x[1])
print(f"数学成绩最高的学生: {top_math_student[0]}, 分数: {top_math_student[1]}")

# 计算每门课的平均分
subjects = ["math", "english", "science"]
subject_averages = {}
for subject in subjects:
    total = sum(student["scores"][subject] for student in students)
    average = total / len(students)
    subject_averages[subject] = average

print("各科平均分:")
for subject, avg in subject_averages.items():
    print(f"{subject}: {avg:.2f}")