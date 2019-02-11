# 第三方库requests的使用

import requests,json

host = "http://httpbin.org/"
endpoint = "get"

url = ''.join([host, endpoint])
params1 = {"show_env":"1"}
headers = {"User-Agent":"test request headers"}

r = requests.get(url)
r = requests.get(url=url, headers=headers,params=params1)
#response = r.json()

print(eval(r.text)['headers']['User-Agent'])
print(r.url)