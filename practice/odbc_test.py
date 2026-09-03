
import pyodbc

# 构建连接字符串
conn_str = (
    "DRIVER=/opt/cloudera/impalaodbc/lib/universal/libclouderaimpalaodbc.dylib;"  # 驱动名称，需与安装的完全一致
    "Host=gamma.demo.sensorsdata.cn;"  # 你的 Impala 服务主机名或IP
    "Port=8416;"  # Impala 默认端口
    #"Database=horizon_default_1;"  # 可选，指定默认数据库
    # 认证方式及其他高级设置请根据情况添加，详见下方说明
    "UID=yhzc;"
    "PWD=#K-1BuaIazlbbFP6lZoUt3szy4iklDAPbBQ;"
    "AuthMech=3;"
)

try:
    # 建立连接
    conn = pyodbc.connect(conn_str, autocommit=True)
    cursor = conn.cursor()

    # 执行一个测试查询
    cursor.execute("select * from horizon_default_1.events limit 1/*sa(default)*/;")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()
except pyodbc.Error as e:
    print(f"连接或查询失败: {e}")