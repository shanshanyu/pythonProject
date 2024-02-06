'''
create_time: 2024/2/6 09:44
author: yss
version: 1.0
通过这个脚本可以验证：在导入模块的时候，其实就是把模块导入到当前模块中
在import_mod模块中只有一行代码：import my_operator，其实就是把 my_operator模块导入到 import_mod 模块中，变成import_mod模块对象的一个属性
import_mod.my_operator

在当前模块中导入 import_mod模块就可以使用这个模块的属性
'''
import import_mod
print(type(import_mod.my_operator))  #通过这行代码验证