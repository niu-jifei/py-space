"""
常用函数


输入与输出
函数 / 参数	功能说明
print	输出指定内容
objects	要输出的内容
sep	输出多个内容时的分隔符
end	结尾追加的内容
file	输出位置（默认控制台）
flush	是否立即刷新输出
input()	获取用户输入





类型转换
函数	功能说明
int()	转为整数
float()	转为浮点数
str()	转为字符串
bool()	转为布尔值
list()	转为列表
tuple()	转为元组
set()	转为集合
dict()	转为字典


数学相关
函数	功能说明
abs()	取绝对值
round()	银行家舍入法：小于5舍，大于5入，等于5看奇偶（奇入偶舍）
pow(a, b)	计算 a 的 b 次方
pow(a, b, c)	计算 a 的 b 次方后，再对 c 取模
divmod(a, b)	返回 (商, 余数)
max()	最大值（支持 key）
min()	最小值（支持 key）
sum()	求和
map()	加工一组数据
filter()	按条件过滤数据
reduce()	合并计算（需 functools.reduce）
sorted()	排序（支持 key）


数据容器相关
函数	功能说明
len()	获取容器中元素个数
range()	生成数字序列（常用于循环）
enumerate()	为序列添加索引
zip()	将多个序列一一配对



类型判断与对象相关
函数	功能说明
type()	查看对象类型
isinstance(obj, type)	判断对象是否属于某个类型
issubclass(A, B)	判断类 A 是否为类 B 的子类
id()	查看对象的内存地址


逻辑判断相关
函数	功能说明
all()	所有元素为真时返回 True
any()	至少一个为真返回 True

字符串辅助相关
函数	功能说明
ord()	获取字符的 Unicode 编码值
chr()	将 Unicode 编码值转换为字符
"""
