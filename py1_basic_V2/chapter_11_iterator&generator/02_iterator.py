"""
迭代器（iterator）

调用__iter__()方法会得到：迭代器(iterator)

备注1：__iter__是一个魔法方法，当调用iter函数时，__iter__会自动调用。

备注2：可迭代对象.__iter__() 等价于： iter(可迭代对象)。

备注3：如果iter(obj)能得到一个迭代器(iterator)，那obj就是可迭代对象。


迭代器(iterator)是一个对象，对象有__next__方法。

迭代器(iterator)对象调用__next__方法 每次调用都会根据当前的状态，返回下一个元素

备注1：迭代器.__next__() 等价于 next(迭代器)。
备注2：当所有元素全都取出后，若继续调用__next__，Python会抛出StopIteration异常，表示迭代结束



迭代器(iterator)对象调用__next__()方法会得到下一个元素。
迭代器(iterator)对象调用__next__()方法会得到一个 StopIter


"""

names = ["张三", "李四", "王五"]
citys = ("北京", "上海", "深圳")
msg = "hello"

print(names.__iter__())
print(citys.__iter__())
print(msg.__iter__())

print(iter(names))
print(iter(citys))
print(iter(msg))


it = iter(names)
print(it.__next__())
print(it.__next__())
print(it.__next__())
# print(it.__next__())  # StopIteration

print("--------------for循环--------------")
names = ["张三", "李四", "王五"]
for item in names:
    print(item)


print("--------------for循环背后的逻辑--------------")
names = ["张三", "李四", "王五"]
# 1️⃣调用【可迭代对象的__iter__方法】获取到一个迭代器(iterator)
it = iter(names)
# 2️⃣开启一个无限循环
while True:
    try:
        # 3️⃣调用__next__方法，获取下一个元素
        item = next(it)
        print(item)
    except StopIteration:
        # 4️⃣捕获 StopIteration 异常，随后结束循环
        break


print("--------------迭代器的__iter__()方法--------------")
# 迭代器（iterator）也拥有__iter__方法，并且其返回值是迭代器自身。
# 这么设计的原因：让 for 循环也能遍历迭代器（即：为了让 iter(迭代器) 不出错）

names = ["张三", "李四", "王五"]

it = iter(names)
print(it)

result = iter(it)
print(result)

print(result.__iter__())

x = iter(result)
print(x)

it = iter(names)
for item in it:
    print(item)


print("--------------迭代器协议--------------")

# 迭代器协议：一个对象如果同时满足如下规范，那该对象就是一个迭代器：
# 1.能被iter()接受。
# 2.能被next()一步一步取值。
# 3.迭代器是一次性的，状态只会向前推进，且不会自动重置（迭代器在遍历的过程中会被“消耗”）

names = ["张三", "李四", "王五"]
it1 = iter(names)
it2 = iter(names)

print(it1)
print(it2)

print(next(it1))
print(next(it1))
print(next(it1))
# print(next(it1))  # 此行代码会抛出异常，因为此时迭代器已经被耗尽了

# 如想重新依次获取元素，需要使用新的迭代器it2
print(next(it2))
print(next(it2))
print(next(it2))
