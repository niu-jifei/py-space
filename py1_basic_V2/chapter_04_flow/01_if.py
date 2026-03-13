# 分支

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
