'''
集合是一种：无序、元素唯一的容器类型。

📋备注：无序是指从集合中取出元素的顺序，与定义集合时存入的顺序不一定一致。

集合分为两种，分别是：

1.可变集合（set）：内部的元素无序（不保证顺序）、不能通过下标访问元素、会自动去除重复元素。
2.不可变集合（forzenset）：特点和可变集合一样，唯一的区别就是：其中的元素不可修改。


1.无序：集合中的元素没有固定顺序，无法通过下标访问。
2.不重复：集合会自动去重，同一个元素只会保留一份。
3.分为两种：可变集合合（set）和不可变集合（forzenset）。
4.集合中的元素必须是不可变类型（如：数字、字符串、元组）。
5.集合支持：并集、交集、差集、对称差集等数学操作。
📍一句话总结：集合是可以去重的数据容器，当只关心元素是否存在，而不在乎顺序的时，首选集合。
'''

# 定义有内容的【可变集合】
print("=== 【可变集合】 ===")
s1 = {10, 20, 20, 30, 40, 40, 50, 60, 60, 70, 80, 90, 100}
s2 = {'你好', 'hello', '你好', 'atguigu', '北京'}
s3 = {10, '你好', True, 1, 12.4}
print(type(s1), s1)  # <class 'set'> {100, 70, 40, 10, 80, 50, 20, 90, 60, 30}
print(type(s2), s2)  # <class 'set'> {'atguigu', 'hello', '你好', '北京'}
print(type(s3), s3)  # <class 'set'> {True, 10, '你好', 12.4}



# 创建【空集合】
s1 = set()
print(type(s1), s1)  # <class 'set'> set()


# s2 = {}   注意：不能直接写{}来定义空集合，因为直接写{}定义的是：空字典。
# print(type(s2), s2)  # <class 'dict'> {}


# 创建【不可变集合】
# 不可变集合的定义方式：借助内置的forzenset函数
# 定义有内容的【不可变集合】
print("=== 【不可变集合】 ===")
s1 = frozenset({10, 20, 20, 30, 40, 40, 50, 60, 60, 70, 80, 90, 100})
s2 = frozenset({'你好', 'hello', '你好', 'atguigu', '北京'})
s3 = frozenset({10, '你好', True, 1, 12.4})
print(type(s1), s1)
print(type(s2), s2)
print(type(s3), s3)

# frozenset 接收的参数，可以是任意可迭代对象，但最终返回的一定是【不可变集合】
s1 = frozenset([10, 20, 30, 40, 50, 50])
s2 = frozenset((10, 20, 30, 40, 50, 50))
s3 = frozenset('hello')
print(type(s1), s1)
print(type(s2), s2)
print(type(s3), s3)

# 定义空集合（不可变集合）
s3 = frozenset()
print(type(s3), s3)


# 集合中不能嵌套【可变集合】，但可以嵌套【不可变集合】
# 通俗理解：只有“不可变”的东西，才能安全的放进集合里
s1 = {10, 20, 30, 40, 50}
s2 = frozenset({100, 200, 300, 400, 500})
l1 = [666, 777, 888]
t1 = ('hello', 'atguigu', '北京')

# s3 = {11, 22, 33, s1}  # 报错
s3 = {11, 22, 33, s2}  # 没问题
# s3 = {11, 22, 33, l1}  # 报错
s3 = {11, 22, 33, t1}  # 没问题
print(s3)


print("===增删改查===")

# add方法：向集合中添加元素
s1 = {10, 20, 30, 40, 50}
s1.add(60)
print(s1)

# update方法：向集合中添加元素（必须传递可迭代对象，例如：列表、元组、集合等）
s1 = {10, 20, 30, 40, 50}
s1.update([60, 70])
s1.update((80, 90))
s1.update({100, 200})
s1.update(range(300, 308))
print(s1)


# remove方法：从集合中移除元素（移除不存在的元素，会报错）
s1 = {10, 20, 30, 40, 50}
s1.remove(20)
print(s1)

# discard方法：从集合中移除元素（移除不存在的元素，不会报错）
s1 = {10, 20, 30, 40, 50}
s1.discard(80)
print(s1)

# pop方法：从集合中移除一个任意元素，返回值是移除的那个元素
print("===pop===")
s1 = {10, 20, 30, 40, 50}
s2 = {'你好', '北京', '尚硅谷', 'hello'}
result = s1.pop()
print(s1)
print(result)

# clear方法：清空集合
s1 = {10, 20, 30, 40, 50}
s1.clear()
print(s1)

# 集合没有下标，也不支持replace方法，所以集合没有专门用于“改”的方法，但可以使用：remove+add的组合，来达到“修改”的效果。
# 改
# 使用 add + remove 的组合，来实现修改的效果
s1 = {10, 20, 30, 40, 50}
s1.remove(20)
s1.add(66)
print(s1)

# 查：集合不能通过下标去读取元素，但能通过 【成员运算符】去查看集合中是否包含指定元素
# 由于成员运算符适用于所有数据容器，所以我们会等所有数据容器都讲完以后，再说成员运算符
s1 = {10, 20, 30, 40, 50}
# s1[0] # 此行报错，因为集合不能通过下标访问元素

# 先提前感受一下成员运算符
result = 20 not in s1
print(result)


print("===常用方法===")

# 集合A.difference(集合B)：
# 作用：找出集合A中，不同于集合B的元素（集合A 与 集合B 都不变，返回的是一个新的集合）
print("===difference===")
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
result = s1.difference(s2)
print(s1)
print(s2)
print(result)


# 集合A.difference_update(集合B)：
# 作用：从集合A中，删除集合B中存在的元素（集合A会被修改，集合B不会）
print("===difference_update===")
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
s1.difference_update(s2)
print(s1)
print(s2)

# 集合A.union(集合B)：
# 作用：合并两个集合，集合A 和 集合B 都不变，返回的是一个新的集合
print("===union===")
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
result = s2.union(s1)
print(s1)
print(s2)
print(result)


# 集合A.issubset(集合B)：
# 作用：判断集合A是否为集合B的子集
# 如果 集合A的所有元素都在集合B中，那就返回True，否则返回False
print("===issubset===")
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
s3 = {30, 40, 50}
result = s3.issubset(s1)
print(result)

# 集合A.issuperset(集合B)：
# 作用：判断集合A是否是集合B的超集
# 如果集合A中，包含了集合B中的所有元素，那就返回True，否则返回False
print("===issuperset===")
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
s3 = {30, 40, 50}
result = s1.issuperset(s3)
print(result)

# 集合A.isdisjoint(集合B)：
# 作用：
# 如果没有交集，返回True；只要有一个公共元素，就返回False
print("===isdisjoint===")
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
s3 = {80, 90}
result = s1.isdisjoint(s2)
print(result)


print("===集合的数学运算===")
s1 = {10, 20, 30, 40, 50, 60}
s2 = {40, 50, 60, 70, 80, 90}

# 并集
result = s1 | s2
print(result) # {70, 40, 10, 80, 50, 20, 90, 60, 30}

# 交集
result = s1 & s2
print(result) # {40, 50, 60}

# 差集
result = s1 - s2
print(result) # {10, 20, 30}

# 对称差集 （并集 - 交集）
result = s1 ^ s2
print(result) # {70, 10, 80, 20, 90, 30}


print("===集合的循环遍历===")
s1 = {10, 20, 30, 40, 50, 60}

# 集合不能使用while循环遍历（以下是错误示例）
# index = 0
# while index < len(s1):
#     print(s1[index])
#     index += 1

# 集合可以使用for循环遍历
for item in s1:
    print(item)