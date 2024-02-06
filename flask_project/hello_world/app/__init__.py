# 2024/2/5 21:13
from flask import Flask
app = Flask(__name__)
from . import routes  #把routes模块导入到包中    app.routes
