"""
异常处理不是让异常消失，而是将异常捕获到，随后根据异常的具体情况，来执行指定的逻辑。

核心规则如下：
1.将可能出现异常的代码放在try中，出现异常后的处理代码写在except中。
2.如果try中的代码出现异常，那try中的后续代码不会执行，并自动跳转到except中。
3.如果try中的代码没有异常，那except中的代码就不会执行。
4.无论是否发生异常，try-except后面的代码都会继续执行。
直接写except捕获到Python中所有的异常 ———— 实际开发中不推荐这样做
"""

# print("=== 捕获异常===")
# try:
#     a = int(input("请输入第一个数："))
#     b = int(input("请输入第二个数："))
#     result = a / b
#     print(f"{a}除以{b}的结果是：{result}")
# except:
#     print("抱歉，程序出现了异常！")
# print("*******我是后续的其它逻辑1*******")
# print("*******我是后续的其它逻辑2*******")


# print("=== 捕获指定的类型的异常===")
# try:
#     a = int(input("请输入第一个数："))
#     b = int(input("请输入第二个数："))
#     result = a / b
#     print(f"{a}除以{b}的结果是：{result}")
# except ZeroDivisionError:
#     print("程序异常：0不能作为除数！")
# except ValueError:
#     print("程序异常：您输入的必须是数字！")
# print("*******我是后续的其它逻辑1*******")
# print("*******我是后续的其它逻辑2*******")

# print("=== 验证异常类之间的继承关系===")
# print(issubclass(ZeroDivisionError, ArithmeticError))
# print(issubclass(ZeroDivisionError, Exception))
# print(issubclass(ValueError, Exception))
# print(issubclass(KeyboardInterrupt, Exception))
# print(issubclass(KeyboardInterrupt, BaseException))


# print("=== 多个 except 处理异常===")
# """
# 多个except从上往下匹配，匹配成功后不再向下匹配
# """
# try:
#     a = int(input("请输入第一个数："))
#     b = int(input("请输入第二个数："))
#     print(x)
#     result = a / b
#     print(f"{a}除以{b}的结果是：{result}")
# except ZeroDivisionError:
#     print("程序异常：0不能作为除数！")
# except ValueError:
#     print("程序异常：您输入的必须是数字！")
# except Exception:
#     print("程序异常!")
# print("*******我是后续的其它逻辑1*******")
# print("*******我是后续的其它逻辑2*******")


# print("=== 获取异常的具体信息===")
# """
# 通过e变量，可以获取异常相关的信息，也可以借助traceback去格式化异常信息
# """
# try:
#     a = int(input("请输入第一个数："))
#     b = int(input("请输入第二个数："))
#     print(x)
#     result = a / b
#     print(f"{a}除以{b}的结果是：{result}")
# except ZeroDivisionError:
#     print("程序异常：0不能作为除数！")
# except ValueError:
#     print("程序异常：您输入的必须是数字！")
# except Exception as e:
#     print(f"⚠程序异常，异常信息：{e}")
#     print(f"⚠程序异常，异常类型：{type(e)}")
#     print(f"⚠程序异常，异常参数：{e.args}")
#     print(f"⚠程序异常，异常的文件：{e.__traceback__.tb_frame.f_code.co_filename}")
#     print(f"⚠程序异常，异常的具体行数：{e.__traceback__.tb_lineno}")
#     # 通过 traceback 来回溯异常
#     import traceback

#     print(traceback.format_exc())
# print("*******我是后续的其它逻辑1*******")
# print("*******我是后续的其它逻辑2*******")


print("=== 一个 except 捕获不同的异常===")
try:
    a = int(input("请输入第一个数："))
    b = int(input("请输入第二个数："))
    print(x)
    result = a / b
    print(f"{a}除以{b}的结果是：{result}")
except (ZeroDivisionError, ValueError, Exception) as e:
    if isinstance(e, ZeroDivisionError):
        print("程序异常：0不能作为除数！")
    elif isinstance(e, ValueError):
        print("程序异常：您输入的必须是数字！")
    else:
        print(f"程序异常：{e}")
print("*******我是后续的其它逻辑1*******")
print("*******我是后续的其它逻辑2*******")
