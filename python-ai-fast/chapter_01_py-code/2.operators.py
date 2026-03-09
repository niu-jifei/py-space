# 案例演示python的所有运算符

# 1. 算术运算符
print("=== 算术运算符 ===")
a = 10
b = 3
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")  # 加法
print(f"a - b = {a - b}")  # 减法
print(f"a * b = {a * b}")  # 乘法
print(f"a / b = {a / b}")  # 除法（浮点数）
print(f"a // b = {a // b}")  # 整除
print(f"a % b = {a % b}")  # 取模
print(f"a ** b = {a ** b}")  # 幂运算
print()

# 2. 比较运算符
print("=== 比较运算符 ===")
x = 5
y = 10
print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")  # 等于
print(f"x != y: {x != y}")  # 不等于
print(f"x > y: {x > y}")  # 大于
print(f"x < y: {x < y}")  # 小于
print(f"x >= y: {x >= y}")  # 大于等于
print(f"x <= y: {x <= y}")  # 小于等于
print()

# 3. 逻辑运算符
print("=== 逻辑运算符 ===")
p = True
q = False
print(f"p = {p}, q = {q}")
print(f"p and q: {p and q}")  # 逻辑与
print(f"p or q: {p or q}")  # 逻辑或
print(f"not p: {not p}")  # 逻辑非
print()

# 4. 赋值运算符
print("=== 赋值运算符 ===")
c = 20
print(f"初始值 c = {c}")
c += 5  # 等同于 c = c + 5
print(f"c += 5, c = {c}")
c -= 3  # 等同于 c = c - 3
print(f"c -= 3, c = {c}")
c *= 2  # 等同于 c = c * 2
print(f"c *= 2, c = {c}")
c /= 4  # 等同于 c = c / 4
print(f"c /= 4, c = {c}")
c //= 2  # 等同于 c = c // 2
print(f"c //= 2, c = {c}")
c %= 3  # 等同于 c = c % 3
print(f"c %= 3, c = {c}")
c **= 2  # 等同于 c = c ** 2
print(f"c **= 2, c = {c}")
print()

# 5. 位运算符
print("=== 位运算符 ===")
m = 12  # 二进制: 1100
n = 6   # 二进制: 0110
# bin 以二进制表示
print(f"m = {m} (二进制: {bin(m)})")
print(f"n = {n} (二进制: {bin(n)})")
print(f"m & n = {m & n} (二进制: {bin(m & n)})")  # 按位与
print(f"m | n = {m | n} (二进制: {bin(m | n)})")  # 按位或
print(f"m ^ n = {m ^ n} (二进制: {bin(m ^ n)})")  # 按位异或
print(f"~m = {~m} (二进制: {bin(~m)})")  # 按位取反
print(f"m << 2 = {m << 2} (二进制: {bin(m << 2)})")  # 左移
print(f"m >> 2 = {m >> 2} (二进制: {bin(m >> 2)})")  # 右移
print()

# 6. 成员运算符
print("=== 成员运算符 ===")
my_list = [1, 2, 3, 4, 5]
my_string = "hello world"
print(f"列表: {my_list}")
print(f"3 in my_list: {3 in my_list}")  # 在列表中
print(f"6 not in my_list: {6 not in my_list}")  # 不在列表中
print(f"'hello' in my_string: {'hello' in my_string}")  # 在字符串中
print(f"'python' not in my_string: {'python' not in my_string}")  # 不在字符串中
print()

# 7. 身份运算符
print("=== 身份运算符 ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = list1")
print(f"list1 is list3: {list1 is list3}")  # 是同一个对象
print(f"list1 is not list2: {list1 is not list2}")  # 不是同一个对象
print(f"list1 == list2: {list1 == list2}")  # 值相等但不是同一个对象
print()

# 8. 运算符优先级示例
print("=== 运算符优先级示例 ===")
result = 2 + 3 * 4  # 先乘后加
print(f"2 + 3 * 4 = {result}")
result = (2 + 3) * 4  # 括号改变优先级
print(f"(2 + 3) * 4 = {result}")
result = 2 + 3 * 4 ** 2  # 幂运算优先级最高
print(f"2 + 3 * 4 ** 2 = {result}")
result = (2 + 3 * 4) ** 2  # 括号改变优先级
print(f"(2 + 3 * 4) ** 2 = {result}")
print()

# 9. 三元运算符
print("=== 三元运算符 ===")
age = 20
status = "成年" if age >= 18 else "未成年"
print(f"年龄: {age}, 状态: {status}")
age = 15
status = "成年" if age >= 18 else "未成年"
print(f"年龄: {age}, 状态: {status}")
print()

# 10. 字符串运算符
print("=== 字符串运算符 ===")
str1 = "Hello"
str2 = "World"
print(f"str1 = '{str1}', str2 = '{str2}'")
print(f"str1 + str2 = '{str1 + str2}'")  # 字符串连接
print(f"str1 * 3 = '{str1 * 3}'")  # 字符串重复
print(f"'lo' in str1: {'lo' in str1}")  # 子字符串检查
print()