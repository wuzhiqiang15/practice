import requests,json

host = "http://httpbin.org/"
endpoint = "post"
url = ''.join([host, endpoint])

data = {"sites":[
    {"name": "test", "url": "www.test.com"},
    {"name": "google", "url": "www.google.com"},
    {"name": "weibo", "url": "www.weibo.com"}
]}

headers = {"User-Agent": "test request headers 222"}

params = {'key1': 'params1', 'key2': 'params2'}


#r = requests.post(url, data=data)
#r = requests.post(url, json=data)
#r = requests.post(url, headers=headers)
r= requests.post(url, params=params)

print(r.json())