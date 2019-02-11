# 使用PyMYSQL第三方库去连接mysql数据库
import pymysql

# 打开数据库连接（参数分别是hosts，账号、密码、数据库名）
db = pymysql.connect("120.26.9.167", "developer", "developer_meiyou_01","app_db")

# 使用cursor()方法获取操作游标
cursor_1 = db.cursor()

# SQL查询语句
sql = "SELECT * FROM brand_area WHERE is_active = 1 LIMIT 5"

try:
    # 执行SQL语句
    cursor_1.execute(sql)
    # 获取所有查询记录列表
    results = cursor_1.fetchall()   # fetchall()方法: 接收全部的返回结果行。
    # 这里要用for循环，从刚刚获取的结果集中获取想要的数据
    for row in results:
        id = row[0]
        name = row[1]
        start_at = row[16]
        end_at = row[17]
        # 打印查询结果
        print("id=%s,name=%s,start_at=%s,end_at=%s" % \
              (id, name, start_at, end_at))
except:
    print("Error:没能获取到数据")

# 关闭数据库连接（一定要记得！）
db.close()