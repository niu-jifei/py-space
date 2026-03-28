print("我是trade模块的__init__.py文件")

a = 100
b = 200


"""
相对导入语法说明
from . import order1 - 导入同一包内的 order1 模块
from .order1 import create_order - 导入同一包内 order1 模块的 create_order 函数
from .. import xxx - 导入父包中的模块

"""
from . import order1

# order1.create_order()


__all__ = ["order1", "pay1"]
