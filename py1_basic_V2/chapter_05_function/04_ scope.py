# 6. 函数作用域


print("=== 函数作用域 ===")
global_var = "全局变量"

def scope_demo():
    # 先声明全局变量
    global global_var

    local_var = "局部变量"
    print(f"函数内部访问全局变量: {global_var}")
    print(f"函数内部访问局部变量: {local_var}")
    
    # 修改全局变量
    global_var = "修改后的全局变量"
    print(f"修改后的全局变量: {global_var}")

scope_demo()
print(f"函数外部访问全局变量: {global_var}")


# 全局作用域 与 局部作用域，以及global的使用
a = 100
b = 200

def test():
    c = '尚硅谷'
    d = '你好啊'
    global a
    a = 300
    print('函数中的打印（a）', a)
    print('函数中的打印（b）', b)
    print('函数中的打印（c）', c)
    print('函数中的打印（d）', d)
test()
print('***************')
print('全局的打印（a）', a)
print('全局的打印（b）', b)
# print(c)
# print(d)