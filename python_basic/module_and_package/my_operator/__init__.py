# 2024/2/5 21:49
from .add import add_func  #把add模块中的add_func程序单元导入到 my_operator包中,在调用时使用my_operator.add_func
from . import sub          #把sub模块导入到 my_operator 包中，在调用的使用需要使用 my_operator.sub.sub_func(xx)
#没必要用这样导，默认python可以这样使用my_operator.sub.sub_func(xx)