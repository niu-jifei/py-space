# 案例演示：Python 的异常处理

# 1. 基本异常处理
print("=== 基本异常处理 ===")
try:
    num = int(input("请输入一个整数: "))
    result = 10 / num
    print(f"10 除以 {num} 的结果是: {result}")
except ValueError:
    print("输入错误: 请输入一个有效的整数")
except ZeroDivisionError:
    print("错误: 不能除以零")
except Exception as e:
    print(f"发生未知错误: {e}")
else:
    print("计算成功完成")
finally:
    print("异常处理结束\n")

# 2. 多种异常类型演示
print("=== 多种异常类型演示 ===")
exception_list = [ValueError, TypeError, IndexError, KeyError, FileNotFoundError]

for i, exc_type in enumerate(exception_list):
    try:
        if exc_type == ValueError:
            int("abc")
        elif exc_type == TypeError:
            "2" + 3
        elif exc_type == IndexError:
            lst = [1, 2, 3]
            print(lst[5])
        elif exc_type == KeyError:
            dct = {"name": "张三"}
            print(dct["age"])
        elif exc_type == FileNotFoundError:
            with open("不存在的文件.txt", "r") as f:
                content = f.read()
    except Exception as e:
        print(f"异常 {i+1}: {type(e).__name__}: {e}")
print()

# 3. 嵌套异常处理
print("=== 嵌套异常处理 ===")
try:
    try:
        # 内层try块
        num1 = int(input("请输入第一个数字: "))
        num2 = int(input("请输入第二个数字: "))
        result = num1 / num2
    except ValueError:
        print("内层异常: 请输入有效的数字")
        raise  # 重新抛出异常
except ZeroDivisionError:
    print("外层异常: 不能除以零")
except ValueError:
    print("外层异常: 捕获到内层重新抛出的ValueError")
else:
    print(f"计算结果: {result}")
print()

# 4. 自定义异常
print("=== 自定义异常 ===")
class AgeError(Exception):
    """自定义年龄异常"""
    def __init__(self, age, message="年龄必须在0-120之间"):
        self.age = age
        self.message = message
        super().__init__(f"{message}, 输入的年龄: {age}")

def check_age(age):
    if age < 0 or age > 120:
        raise AgeError(age)
    return f"年龄 {age} 有效"

# 测试自定义异常
test_ages = [25, -5, 150, 80]
for age in test_ages:
    try:
        print(check_age(age))
    except AgeError as e:
        print(f"捕获到自定义异常: {e}")
print()

# 5. 异常链和异常上下文
print("=== 异常链和异常上下文 ===")
try:
    try:
        # 尝试处理一个可能引发异常的操作
        data = {"name": "张三", "age": "二十五"}
        # 这里会引发TypeError，因为age是字符串不是数字
        age = int(data["age"])  
    except TypeError as e:
        # 使用raise from创建异常链
        raise ValueError("年龄必须是数字") from e
except ValueError as e:
    print(f"捕获到异常: {e}")
    print(f"原始异常: {e.__cause__}")
print()

# 6. 使用assert进行断言检查
print("=== 断言检查 ===")
def calculate_discount(price, discount):
    assert price > 0, "价格必须大于0"
    assert 0 <= discount <= 1, "折扣必须在0到1之间"
    return price * (1 - discount)

# 测试断言
test_cases = [
    (100, 0.2),   # 正常情况
    (50, 0.5),    # 正常情况
    (-10, 0.1),   # 会触发断言错误
    (100, 1.5)    # 会触发断言错误
]

for price, discount in test_cases:
    try:
        new_price = calculate_discount(price, discount)
        print(f"原价: {price}, 折扣: {discount}, 折后价: {new_price}")
    except AssertionError as e:
        print(f"断言错误: {e}")
print()

# 7. 使用with语句进行资源管理
print("=== 资源管理 ===")
try:
    # 使用with语句自动管理文件资源
    with open("example.txt", "w", encoding="utf-8") as f:
        f.write("这是一个示例文件\n")
        f.write("用于演示with语句的资源管理")
    
    # 读取文件内容
    with open("example.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print("文件内容:")
        print(content)
except FileNotFoundError:
    print("文件不存在")
except IOError as e:
    print(f"文件操作错误: {e}")
finally:
    # 清理资源（如果文件存在）
    import os
    if os.path.exists("example.txt"):
        os.remove("example.txt")
        print("示例文件已删除")
print()

print("异常处理演示完成")