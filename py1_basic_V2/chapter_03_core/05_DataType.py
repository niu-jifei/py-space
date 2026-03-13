'''
数据类型
'''

# 数值类型： 整数 浮点数 复数
# 布尔类型： 布尔真值 布尔假值
# 字符串类型： 字符串 多行字符串   四种定义方式：单引号，双引号，三个单引号，三个双引号

# 列表类型： 列表 空列表
# 元组类型： 元组 单元素元组
# 集合类型： 集合 空集合
# 字典类型： 字典 空字典
# None类型： None

# type() # 查看数据类型

# 使用变量接收 type() 返回的类型
result1 = type('张三')
result2 = type(18)
result3 = type(72.5)

print(result1) # <class 'str'> 注意此处返回的不是string，是 string 的简写：str
print(result2) # <class 'int'>
print(result3) # <class 'float'>


# 字符串格式化
name = '张三'
gender = '男'
weight = 65.2
age = 12

# 字符串拼接
info1 = '我叫' + name + '，我是' + gender + '生'
print(info1)

# 占位符
info2 = '我叫%s，我是%s生，体重%.2fkg' % (name, gender, weight)
print(info2)
info3 = '我叫{0}，我是{1}生，体重{2:.2f}kg'.format(name, gender, weight)
print(info3)

# f-string 
info4 = f'我叫{name}，我是{gender}生，体重{weight:.2f}kg'
print(info4)


# 占位符精度控制 m.n m 表示整数部分，n 表示小数部分
info5 = '我叫%3.3s，我是%3.2s生，体重%3.2fkg' % (name, gender, weight)
print(info5)

# 转义字符
info6 = '我叫\n张三'
print(info6)

print(' 使用 \' 包裹一个字符串')

# 使用 \' 输出 '
print('在Python中，可以使用\'包裹一个字符串')

# 使用 \" 输出 "
print("在Python中，可以使用\"包裹一个字符串")

# 使用 \n 进行换行
print('注册会员需要以下信息：\n姓名\n年龄\n手机号')

# 使用 \\ 输出 \
print('D:\\nice')

# 使用 \b 删除前一个字符
print('helloo\b')

# 使用 \r 使光标回到本行开头，覆盖输出
print('67%\r68%')

# 使用 \t 表示水平制表符（让光标跳转到下一个制表位）
# 一个制表位到底是几位，是不确定的，但我们可以通过在字符串后面加.expandtabs()来指定位数。
print('1234123412341234')
print('ab\tcd.expandtabs(4)')
print('abc\td.expandtabs(4)')
print('abcd\ta.expandtabs(4)')
print('我是\t中文.expandtabs(4)')
print('12341234123412341234')
print('姓名\t性别\t年龄')
print('张三\t男\t\t18')
print('李四\t女\t\t25')
print('王五\t男\t\t32')