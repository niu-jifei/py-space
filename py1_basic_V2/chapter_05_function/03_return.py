# 返回值

# 1. 无返回值
# 定义函数
def add(n1, n2):
    print(f'我收到了：{n1}、{n2}，二者相加是：{n1 + n2}')
    print('add函数执行完毕了')

# 调用函数
result = add(100, 200)
print(result)  # None

# 2. 有返回值
# 定义函数
def add(n1, n2):
    print(f'我收到了：{n1}、{n2}，二者相加是：{n1 + n2}')
    print('add函数执行完毕了')
    return n1 + n2

# 调用函数
result = add(100, 200)
print(result)

# print函数是没有返回值的
res = print('hello')
print(res)

# 3.多个返回值
def calculate(a, b):
    """返回两个数的和、差、积、商"""
    return a + b, a - b, a * b, a / b

# 接收多个返回值
sum_result, diff_result, product_result, quotient_result = calculate(10, 2)
print(f"10 + 2 = {sum_result}")
print(f"10 - 2 = {diff_result}")
print(f"10 * 2 = {product_result}")
print(f"10 / 2 = {quotient_result}")
print()