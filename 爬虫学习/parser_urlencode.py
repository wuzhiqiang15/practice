import urllib.request
from urllib import request
import urllib.parse

if __name__ == "__main__":
    url = "http://www,baidu.com/s?"
    wd = input("请输入搜索词：")
    pd = {"wd": wd}
    pd = urllib.parse.urlencode(pd)
    print(pd)

    fullurl = url + pd
    print(fullurl)

    rsp = request.urlopen(fullurl)
    html = rsp.read()
    html = html.decode()
    print(html)