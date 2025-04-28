'''
date：2025/4/21
desc: 向mysql中插入数据
'''

import pymysql

#链接mysql
conn = pymysql.connect(host='123.60.82.87',port=3306,user='root',password='ZXcv1234!@#$',db='unicom')

#创建游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# #插入数据
# cursor.execute("insert into admin(username,password,mobile) values('admin','1234','12345677')")

#%s 是占位符，不用能字符串格式化，会有sql注入风险
sql = "insert into admin(username,password,mobile) values(%s,%s,%s)"
cursor.execute(sql,['admin','1234','123456781'])

#提交
conn.commit()

#关闭游标和连接
cursor.close()
conn.close()
