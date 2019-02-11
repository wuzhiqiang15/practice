import scrapy


class SimpleUrl(scrapy.Spider):

    name = "simpleurl"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
    # parse()方法来获取数据
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'mingyan-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('保存文件: %s' % filename)
