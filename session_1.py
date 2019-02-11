import requests,json

host = "http://api.youzibuy.com/"
endpoint = "tae_channel_list"

url = ''.join([host, endpoint])

url_2 = "http://api.youzibuy.com/tae_channel_list?app_id=07&platform=ios&v=2.5.1&channel_id=1"

r = requests.get(url)

print('获取到的url信息为：', r.text)
print(r.url)

print('======================================分割线======================================\n')

# 初始化一个session对象
s = requests.session()

# cookie的信息存在了session中
s.get(url_2)

r1 = s.get(url)

print('获取session后的url信息为：', r1.text)