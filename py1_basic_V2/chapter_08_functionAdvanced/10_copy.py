"""
深拷贝

浅拷贝
"""

print("--------赋值---------")
"""
直接赋值
"""
nums1 = [10, 20, 30, 40]
nums2 = nums1
nums2[3] = 99

print(nums1[3])  # 99
print(nums2[3])  # 99


print("--------浅拷贝---------")
"""
浅拷贝
浅拷贝会创建一个新的外层容器，但内部的元素仍然引用原来的对象。 

"""
import copy

nums1 = [10, 20, 30, 40]
nums2 = copy.copy(nums1)
print(id(nums1))
print(id(nums2))

nums2[3] = 99

print(nums1[3])  # 40
print(nums2[3])  # 99
print(nums1)
print(nums2)
print(id(nums1))
print(id(nums2))

"""
嵌套数据仍然是共享的，修改嵌套数据会互相影响
"""
nums1 = [10, 20, 30, [40, 50]]
nums2 = copy.copy(nums1)
print(id(nums1))
print(id(nums2))
print("------nums1-----------")
for index in nums1:
    print(id(index))
print("------nums2-----------")
for index in nums2:
    print(id(index))

nums2[3][0] = 99

print(nums1[3][0])
print(nums2[3][0])


print("--------深拷贝---------")
"""
深拷贝

创建一个新的外层容器，同时对内部所有【可变对象】进行递归复制（不可变对象不复制，继续引用）。

"""
import copy

nums1 = [10, 20, 30, [40, 50]]
nums2 = copy.deepcopy(nums1)
print(id(nums1))
print(id(nums2))

nums2[3][0] = 99


print(nums1)
print(nums2)

print(nums1[3][0])
print(nums2[3][0])

"""
特点：
1.深拷贝可以彻底消除数据之间的相互影响。
2.深拷贝遇到【不可变对象】不会复制，会直接引用。

注意点：
1.深拷贝只复制可变对象，不可变对象会直接引用。
2.元组中如果只包含不可变对象，则深拷贝没有效果。
"""

import copy

a = 666
# a是不可变对象，即便调用deepcopy也不会深拷贝，会直接引用
b = copy.deepcopy(a)

print(id(a))
print(id(b))

import copy


"""
元组中只包含不可变对象，则深拷贝没有效果
"""
nums1 = (10, 20, 30, 40)
nums2 = copy.deepcopy(nums1)

print(id(nums1))
print(id(nums2))

print("-----------------")
"""
元组 (10, 20, 30, [40, 50])本身是不可变对象，即元组的引用和结构不可变（无法添加、删除或替换元素）。
但元组的元素可以是任意类型。本例中，前三个元素（整数 10, 20, 30）是不可变对象，第四个元素（列表 [40, 50]）是可变对象。


深拷贝（copy.deepcopy）的行为：
深拷贝会递归复制所有对象，创建原始对象的完全独立副本。
对于不可变对象（如整数、字符串、不含可变元素的元组），深拷贝通常不会创建新实例，因为不可变对象在内存中可安全共享，修改不会影响原始对象。
对于可变对象（如列表、字典）或包含可变对象的不可变对象（如本例中的元组），深拷贝会创建新的可变对象副本，并保持外层不可变对象的结构。


整数 10, 20, 30可能仍与 nums1共享同一内存地址（因不可变，无需复制）。
列表 [40, 50]会被深拷贝为一个新列表，与 nums3[3]独立。
"""
nums3 = (10, 20, 30, [40, 50])
nums4 = copy.deepcopy(nums3)

print(id(nums3))

print(id(nums4))

print("------nums3-----------")
for index in nums3:
    print(id(index))
print("------nums4-----------")
for index in nums4:
    print(id(index))
