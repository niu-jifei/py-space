def calculate(x, y):
    res1 = x + y
    res2 = x - y
    return res1, res2  # 实际返回的是：(res1, res2)


result = calculate(10, 20)
r1, r2 = calculate(10, 20)
print(result[0])
print(result)  # (30, -10)
print(r1)  # 30
print(r2)  # -10
