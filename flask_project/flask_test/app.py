'''
create_time: 2024/12/9 11:18
author: yss
version: 1.0
'''
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    print(app.name)
    return '<h1>hello flask</h1>'


def main():
    app.run()


if __name__ == '__main__':
    main()