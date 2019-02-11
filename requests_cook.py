# 获取cookies

import requests,json

url = 'https://www.baidu.com/'

r = requests.get(url)

# 将RequestsCookieJar转化为字典
c = requests.utils.dict_from_cookiejar(r.cookies)

print('url的cookies是：', r.cookies)

print('转化为字段后的Cookies为', c)

for a in r.cookies:
    print(a.name, a.value)