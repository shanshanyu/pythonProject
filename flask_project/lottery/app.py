from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/choice', methods=['GET', 'POST'])
def choice():
    member_list = ['a','b','c','d','e','f']
    member = random.choice(member_list)
    return render_template('index.html',member = member)

def main():
    app.run()

if __name__ == '__main__':
    main()