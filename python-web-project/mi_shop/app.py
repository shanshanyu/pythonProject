'''
date：2025/2/19
desc:  小米商城，这里是入口
'''
from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
