# 羊毛提现：校验当存在提现中的订单时，无法再次申请提现
import pymysql
import requests

host = "https://test-youngmall-api.youzibuy.com/"
endpoint = "doDraw"

url = ''.join([host, endpoint])
#print(url)
params = {"auth": "7.m5I6QIvaGCjPk0T7QHA4sXuND12rP-PvY5mg-TGqQAs", "platform": "android", "v": "2.1.1", "myuid": "227990245", "app_id": "23", "amount": "1", "debug": "youngmaildebug"}

# 连接mysql，获取用户是否存在待提现、提现中的订单
db = pymysql.connect("rm-vy1tp2piapdac4vwu.mysql.rds.aliyuncs.com", "youngmall", "K6JkpLpM4kYEkFSa", "youngmall")

cursor = db.cursor()

SQL = "select count(*) from member_draw_orders WHERE uid='227990245' and `status` in (10,12,20)"

try:
    cursor.execute(SQL)
    restults = cursor.fetchall()
    print("用户订单数为：{0}".format(restults[0][0]))
except:
    print("Error：无法获取到数据")

db.close()

# 如果数据库中不存在提现中、待提现的订单，则去请求两次接口，然后查看第二次请求时接口是否会给出重复提现的提示
# 如果数据库中存在提现中、待提现的订单，则请求一次接口

if restults[0][0] == 0:
    doDraw = requests.get(url, params=params)
    print(doDraw.json())
    if doDraw.json()["code"] == '200':
        doDraw_1 = requests.get(url, params=params)
        print(doDraw_1.json())
        assert doDraw_1.json()["code"] == "60004", "断言失败"
else:
    doDraw = requests.get(url, params=params)
    print(doDraw.json())
    assert doDraw.json()["code"] == "60004", "断言失败"
