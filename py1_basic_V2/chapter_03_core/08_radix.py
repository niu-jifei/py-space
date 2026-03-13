'''
进制

二进制：binary / base 2
十进制：decimal / base 10
八进制：octal / base 8
十六进制：hexadecimal / base 16
'''

# 0b开头表示二进制
num1 = 0b11001
# 0o开头表示八进制
num2 = 0o1034
# 0x开头表示十六进制
num3 = 0x1cf

# Python 在对上面的 num1、num2、num3进行计算、打印等操作时，会自动将其转为十进制
print(num1, num2, num3)  # 25  540  463
print(num1 + 1)  # 26
print(str(num2)) # 540
print(num3 > 400) # True


# 进制转换
print(bin(25))

print(oct(450))

print(hex(4563))

print(int('0b11101', 2))
print(int('0o1034', 8))
print(int('0xaf', 16))
