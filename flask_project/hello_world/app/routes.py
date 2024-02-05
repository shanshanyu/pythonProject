# 2024/2/5 21:16
from . import app

@app.route('/')
@app.route('/index')
def index():
    return 'hello wolrd'