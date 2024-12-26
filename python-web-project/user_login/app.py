from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/reg',methods=['GET','POST'])
def reg():
    if request.method == 'GET':
        #在这里接受到客户端GET传过来的数据，处理完成返回
        return render_template('user_signup.html')
    elif request.method == 'POST':
        # 在这里接受到客户端POST传过来的数据，处理完成返回
        print(request.form)
        print(request.form.get('username'))
        print(request.form.getlist('ability'))
        return '注册成功'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('user_login.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('pass')
        print(user,password)
        if request.form.get('user') == 'abc' and request.form.get('pass') == '123':
            print('login success')
            return 'true'
        else:
            print('login failed')
            return 'false'



if __name__ == '__main__':
    app.run()