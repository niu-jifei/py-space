"""
1.由开发人员自己定义一个异常类，用来表示代码中“更具体、更有业务含义”的异常。
2.具体规则：定义一个类（类名通常以Error结尾），继承Exception类或它的子类。
"""


class SchoolNameError(Exception):
    def __init__(self, msg):
        super().__init__("【学校名称异常】" + msg)


def check_school_name(name: str):
    if len(name) > 10:
        raise SchoolNameError("学校名称不能超过10个字符")
    else:
        print("学校名称符合要求")


try:
    check_school_name("上海大学")
except SchoolNameError as e:
    print(f"程序异常：{e}")
