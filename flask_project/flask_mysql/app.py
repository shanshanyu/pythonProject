'''
date：2025/4/22
desc: flask 程序
'''
from flask import Flask,render_template,request
import pymysql

app = Flask(__name__)

@app.route("/add/user",methods=['GET','POST'])
def add_user():
    if request.method == 'GET':
        return render_template("add_user.html")
    elif request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        mobile = request.form.get('mobile')

        #建立连接，创建游标，执行sql，提交，关闭游标，关闭连接
        conn = pymysql.connect(host='123.60.82.87',port=3306,user='root',password='ZXcv1234!@#$',db='unicom')
        cur = conn.cursor()
        sql = "insert into admin(username,password,mobile) values(%s,%s,%s)"
        cur.execute(sql,(user,password,mobile))
        conn.commit()
        cur.close()
        conn.close()

        return '插入成功'


@app.route("/show/user",methods=['GET'])
def show_user():
    # 建立连接，创建游标，执行sql，提交，关闭游标，关闭连接
    conn = pymysql.connect(host='123.60.82.87', port=3306, user='root', password='ZXcv1234!@#$', db='unicom')
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from admin"
    cur.execute(sql)
    data_list = cur.fetchall()
    cur.close()
    conn.close()
    print(data_list)
    return render_template('show_user.html',data_list=data_list)


if __name__ == '__main__':
    app.run(debug=True)