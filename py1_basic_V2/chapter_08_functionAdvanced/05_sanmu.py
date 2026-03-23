"""
条件表达式： 根据不同的条件，得到不同的值，又称：三元表达式，也叫：三目运算符

结果1 if 条件 else 结果2

具体规则： 如果条件为真，整个表达式的结果就是“结果1”，否则就是“结果2”
"""

age = 20

# 传统if-else写法
if age >= 18:
    text = "成年"
else:
    text = "未成年"

# 条件表达式写法
text = "成年" if age >= 18 else "未成年·"
print(text)

# 简单的二选一场景
rain = True
food = "外卖" if rain else "出去吃"

is_vip = True
disscount = 0.8 if is_vip else 1.0

is_login = True
msg = "欢迎回来！" if is_login else "请先登录！"
