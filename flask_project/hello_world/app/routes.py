# 2024/2/5 21:16
from . import app  #从包中导入app模块，后续调用方式为： routes.app  触发了循环导包

@app.route('/')
@app.route('/index')
def index():
    return 'hello wolrd'