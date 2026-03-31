"""
可迭代对象（iterable）、迭代器（iterator）


可迭代对象（iterable）
概念：能被 for 循环遍历的对象，就是可迭代对象（iterable）
如下这些都是可迭代对象（iterable）：
1.字符串
2.列表
3.元组
4.字典
5.集合
6.字节
7.字节数组
8.range

可迭代对象都拥有__iter__方法。


非可迭代对象（iterable）
概念：不能被 for 循环遍历的对象，就是非可迭代对象（non-iterable）

"""

print("------可迭代对象-------")
names = ["张三", "李四", "王五"]
citys = ("北京", "上海", "深圳")
msg = "hello"

names.__iter__()
citys.__iter__()
msg.__iter__()

print(names.__iter__())
print(citys.__iter__())
print(msg.__iter__())

print(hasattr(names, "__iter__"))
print(hasattr(citys, "__iter__"))
print(hasattr(msg, "__iter__"))


print("------非可迭代对象-------")
age = 10


def test():
    pass


print(hasattr(age, "__iter__"))
print(hasattr(test, "__iter__"))
