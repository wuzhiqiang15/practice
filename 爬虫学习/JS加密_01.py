
from urllib import request, parse

def youdao(key):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    # POST请求中的data数据
    data = {
        "action": "FY_BY_REALTIME",
        "bv": "e2a78ed30c66e16a857c5b6486a1d326",
        "client": "fanyideskweb",
        "doctype": "json",
        "from": "AUTO",
        "i": "girl",
        "keyfrom": "fanyi.web",
        "salt": "15445240760649",
        "sign": "21a3fcddf616b65e31715616c51368ec",
        "smartresult": "dict",
        "to": "AUTO",
        "ts": "1544524076064",
        "typoResult": "false",
        "version": "2.1"
    }

    # 必须把POST的data数据进行parse解析，然后再encode转为byte格式
    data = parse.urlencode(data).encode()

    # 请求头信息
    header = {"Host":"fanyi.youdao.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            #"Accept-Encoding": "gzip, deflate",
            "Referer": "http://fanyi.youdao.com/",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Length": "254",
            "Connection": "keep-alive",
            "Cookie": "YOUDAO_MOBILE_ACCESS_TYPE=1; OUTFOX_SEARCH_USER_ID=443858310@10.169.0.83; JSESSIONID=aaaGfCxgXmEhi7weVZCEw; ___rl__test__cookies=1544524076048; OUTFOX_SEARCH_USER_ID_NCOO=1707286803.802219"}

    # 构建一个Request()对象
    # Request存在的意义是便于在请求的时候传入一些信息，如data、header
    req = request.Request(url=url, data=data, headers=header)

    # 使用urlopen()发起请求
    rsp = request.urlopen(req)

    # 使用read()方法读取返回的内容，并使用decode()进行解码
    html = rsp.read().decode()

    print(html)


if __name__ == '__main__':
    youdao("gril")



