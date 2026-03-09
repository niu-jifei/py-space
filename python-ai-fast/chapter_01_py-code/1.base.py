# 演示python的所有数据类型
# 1.声明很多变量，并用到各种数据类型

# 数值类型
integer_var = 42
float_var = 3.14159
complex_var = 3 + 4j

# 布尔类型
bool_true = True
bool_false = False

# 字符串类型
string_var = "Hello, Python!"
multiline_string = """这是多行
字符串示例
包含换行"""

# 列表类型
list_var = [1, 2, 3, "apple", True]
empty_list = []

# 元组类型
tuple_var = (1, 2, 3, "banana", False)
single_tuple = (42,)  # 单元素元组需要逗号

# 集合类型
set_var = {1, 2, 3, 4, 5}
empty_set = set()  # 空集合不能用{}表示

# 字典类型
dict_var = {"name": "张三", "age": 25, "city": "北京"}
empty_dict = {}

# None类型
none_var = None

# 字节类型
bytes_var = b"hello"
bytearray_var = bytearray(b"world")

# 2. 打印这些变量的类型 type(variable)

print("=== 数据类型演示 ===")
print(f"整数类型: {integer_var}, 类型: {type(integer_var)}")
print(f"浮点数类型: {float_var}, 类型: {type(float_var)}")
print(f"复数类型: {complex_var}, 类型: {type(complex_var)}")
print(f"布尔真值: {bool_true}, 类型: {type(bool_true)}")
print(f"布尔假值: {bool_false}, 类型: {type(bool_false)}")
print(f"字符串类型: {string_var}, 类型: {type(string_var)}")
print(f"多行字符串: {repr(multiline_string)}, 类型: {type(multiline_string)}")
print(f"列表类型: {list_var}, 类型: {type(list_var)}")
print(f"空列表: {empty_list}, 类型: {type(empty_list)}")
print(f"元组类型: {tuple_var}, 类型: {type(tuple_var)}")
print(f"单元素元组: {single_tuple}, 类型: {type(single_tuple)}")
print(f"集合类型: {set_var}, 类型: {type(set_var)}")
print(f"空集合: {empty_set}, 类型: {type(empty_set)}")
print(f"字典类型: {dict_var}, 类型: {type(dict_var)}")
print(f"空字典: {empty_dict}, 类型: {type(empty_dict)}")
print(f"None类型: {none_var}, 类型: {type(none_var)}")
print(f"字节类型: {bytes_var}, 类型: {type(bytes_var)}")
print(f"字节数组类型: {bytearray_var}, 类型: {type(bytearray_var)}")

# 3. 编写几个类型转换案例

print("\n=== 类型转换演示 ===")

# 字符串转数字
str_to_int = int("123")
str_to_float = float("3.14")
print(f"字符串'123'转整数: {str_to_int}, 类型: {type(str_to_int)}")
print(f"字符串'3.14'转浮点数: {str_to_float}, 类型: {type(str_to_float)}")

# 数字转字符串
int_to_str = str(456)
float_to_str = str(2.718)
print(f"整数456转字符串: {int_to_str}, 类型: {type(int_to_str)}")
print(f"浮点数2.718转字符串: {float_to_str}, 类型: {type(float_to_str)}")

# 列表、元组、集合相互转换
list_example = [1, 2, 2, 3, 4]
tuple_from_list = tuple(list_example)
set_from_list = set(list_example)
list_from_tuple = list(tuple_var)
print(f"列表转元组: {tuple_from_list}, 类型: {type(tuple_from_list)}")
print(f"列表转集合(去重): {set_from_list}, 类型: {type(set_from_list)}")
print(f"元组转列表: {list_from_tuple}, 类型: {type(list_from_tuple)}")

# 布尔转换
print(f"非零数字转布尔: {bool(42)}, 类型: {type(bool(42))}")
print(f"零转布尔: {bool(0)}, 类型: {type(bool(0))}")
print(f"非空字符串转布尔: {bool('hello')}, 类型: {type(bool('hello'))}")
print(f"空字符串转布尔: {bool('')}, 类型: {type(bool(''))}")
print(f"非空列表转布尔: {bool([1, 2, 3])}, 类型: {type(bool([1, 2, 3]))}")
print(f"空列表转布尔: {bool([])}, 类型: {type(bool([]))}")

# 错误处理示例
print("\n=== 错误处理演示 ===")
try:
    invalid_conversion = int("not_a_number")
except ValueError as e:
    print(f"类型转换错误: {e}")

