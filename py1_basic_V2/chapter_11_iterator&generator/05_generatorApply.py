print("-----用生成器实现遍历Person类的实例对象-----")


class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.__attr = [name, age, gender, address]

    def __iter__(self):
        # yield self.name
        # yield self.age
        # yield self.gender
        # yield self.address
        yield from self.__attr


p1 = Person("张三", 18, "男", "北京昌平")
# 目标：
for attr in p1:
    print(attr)


print("-----生成器实现斐波那契数列-----")


def fibo(total):
    pre = 1
    cur = 1

    for index in range(total):
        if index < 2:
            yield 1
        else:
            value = pre + cur
            pre = cur
            cur = value
            yield value


f1 = fibo(10)

for item in f1:
    print(item)


"""
无论是迭代器，还是生成器对象，都可以用list、tuple、set等直接拿到其里面的所有内容（注意：如果数据量很大，可能会挤爆内存）
"""

print("-----用集合实现斐波那契数列-----")


def fibo(total):
    pre = 1
    cur = 1

    for index in range(total):
        if index < 2:
            yield 1
        else:
            value = pre + cur
            pre = cur
            cur = value
            yield value


f1 = fibo(10)

result = set(f1)
print(result)


print("-----生成器表达式-----")
"""
生成器表达式：一种用类似列表推导式的语法，快速创建生成器对象的方式。
语法格式：(表达式 for 变量 in 可迭代对象)。
什么时候适合用生成器表达式？———— 当“每个结果，只依赖当前这一个元素”时。

列表推导式：[] 方括号
生成器表达式：() 圆括号

二、核心区别（重点）

1. 内存占用
列表推导式：一次性把所有元素载入内存，生成完整列表；数据大时占内存极高。
生成器表达式：惰性求值，一次只生成一个元素，用一个取一个，内存几乎不涨。

2. 运行机制
列表：立刻算完所有结果，存列表。
生成器：迭代时才逐个计算，暂停 / 唤醒（底层靠 yield）。

3. 可复用性
列表：可反复遍历、索引、切片 lst[0]。
生成器：单向迭代，遍历一次就空了，不支持索引 / 切片。

4. 速度
小数据：列表更快（一次性算完）。
超大批量 / 无限数据流：生成器碾压（不爆内存）。


5. 返回类型
[] → list
() → generator
"""
nums = [10, 20, 30, 40]

# 列表推导式
result1 = [n * 2 for n in nums]
print(result1)

# 生成器表达式（和列表推导式很像，不要搞混）
result2 = (n * 2 for n in nums)


for item in result2:
    print(item)

# result2 是一个生成器对象， 只能用一次， 不能重复遍历
result = list(result2)
print(result)
