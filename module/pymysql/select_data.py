'''
date：2025/4/21
desc: 从mysql中查询数据
'''
import pymysql

#链接mysql
conn = pymysql.connect(host='123.60.82.87',port=3306,user='root',password='ZXcv1234!@#$',db='unicom')

#创建游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

sql = 'select * from admin'
cursor.execute(sql)

#得到的数据是 列表里面套字典
result = cursor.fetchall()

#关闭游标和连接
cursor.close()
conn.close()

print(result)