"""
迭代器的优势
1.迭代器是惰性计算，不会一次性生成所有结果，所以能显著降低内存占用。
2.当数据量很大，不确定要用多少结果时，推荐使用迭代器。
"""


class Fibo:
    def __init__(self, total):
        # 要生成多少个数
        self.total = total
        # 当前生成到第几个了（计数器，指针）
        self.index = 0
        # 初始的两个值
        self.pre = 1
        self.cur = 1

    def __iter__(self):
        return self

    def __next__(self):
        # 当生成足够数量后，抛出StopIteration异常
        if self.index >= self.total:
            raise StopIteration
        # 前两项都是1
        if self.index < 2:
            value = 1
        else:
            # 新的结果等于前两项的和
            value = self.pre + self.cur
            # 更新一下pre和cur
            self.pre = self.cur
            self.cur = value
        # 计数器+1
        self.index += 1
        # 返回value
        return value


# 不使用迭代器实现【斐波那契数列】：
def fibo(total):
    if total <= 0:
        return []
    if total == 1:
        return [1]
    nums = [1, 1]
    for i in range(2, total):
        nums.append(nums[-1] + nums[-2])
    return nums


import tracemalloc

# 分析内存占用情况：
# 分别运行如下两段代码后，会发现迭代器实现明显节约内存。
tracemalloc.start()
f1 = Fibo(0)
m = tracemalloc.get_traced_memory()[1]
print(f"内存占用是：{m / 1024 / 1024}MB")

tracemalloc.start()
f1 = fibo(0)
m = tracemalloc.get_traced_memory()[1]
print(f"内存占用是：{m / 1024 / 1024}MB")
