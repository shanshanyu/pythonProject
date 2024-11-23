from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/signup',methods=['GET'])
def signup():
    return render_template('user_signup.html')

@app.route('/user_login')   #用户登录
def user_login():
    return render_template('user_login.html')

@app.route('/do/reg',methods=['GET'])
def do_reg():
    #在这里接受到客户端GET传过来的数据，处理完成返回
    print(request.args)
    return '注册成功'

@app.route('/post/reg',methods=['POST'])
def post_reg():
    # 在这里接受到客户端POST传过来的数据，处理完成返回
    print(request.form)
    return '注册成功'

if __name__ == '__main__':
    app.run()