"""
raise：手动抛出异常。

当程序遇到不符合预期情况时，可以使用raise语句手动触发（抛出）异常。
"""

try:
    age = int(input("请输入年龄："))

    if 18 <= age <= 120:
        print(f"年龄 {age} 符合要求")
    elif 0 <= age < 18:
        print(f"年龄 {age} 不符合要求")
    else:
        raise ValueError(f"年龄 {age} 不符合要求")
except Exception as e:
    print(f"程序异常：{e}")
    print(e)
    print(type(e))
    print(e.args)
    print(e.__traceback__)
    print(e.__cause__)
    print(e.__context__)
    print(e.__suppress_context__)
    print(e.__suppress_context__)
    print(e.__doc__)
    print(e.__module__)
    print(e.__name__)
