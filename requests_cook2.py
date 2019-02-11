# 发送cookies到服务器

import requests,json

host = "http://httpbin.org/"
endpoint = "cookies"

url = ''.join([host, endpoint])

# 方法一：简单发送（先定义一个cookies变量）
'''
cookies = {"aaa":"bbb"}

r1 = requests.get(url, cookies=cookies)

print(r1.text)
'''

# 方法二(相对灵活)
# 先请求一个url，然后获取其cookies，并且转化为dict
r2 = requests.get(url='https://www.baidu.com/', timeout=5)
c2 = requests.utils.dict_from_cookiejar(r2.cookies)   # 获取cookies，并转化为dict

req = requests.get(url, cookies=c2)
print(req.text)


