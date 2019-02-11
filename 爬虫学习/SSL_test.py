# SSL证书就是指遵守SSL安全套阶层协议的服务器数字证书，是由第三方公司（美国网景）开发
# CA 是数字证书认证中心，是发放、管理、废除数字证书的第三方机构
# 遇到不信任的SSL证书，需要单独处理，ssl._create_default_https_context = ssl._create_unverified_context

from urllib import request
import ssl

# 利用非认证上下文环境，替换认证的上下文环境（简单来说就是可以用这个方法，来跳过SSL认证）
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.12306.cn/mormweb/"

#req = request.Request(url)

rsp = request.urlopen(url)

html = rsp.read().decode()

print(html)
