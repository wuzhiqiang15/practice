import scrapy

class itemspider(scrapy.Spider):
    name = "itemspider"
    start_urls = ['http://lab.scrapyd.cn']

    def parse(self, response):
        mingyan = response.css('div.quote') # 提取首页所有符合条件的信息，保存至变量mingyan

        for v in mingyan:
            text = v.css('.text::text').extract_first()  # 提取名言
            autor = v.css('.author::text').extract_first()  # 提取作者
            tags = v.css('.tags .tag::text').extract()  # 提取标签
            tags = ','.join(tags)  # 数组转化为字符串

            #next_page = response.css('li.next a::attr(href)').extract_first()
            #if next_page is not None:
            #    next_page = response.urljoin(next_page)
            #    yield scrapy.Request(next_page, callback=self.parse)


            fileName = '%s-语录.txt' % autor # 爬取的内容存入文件，文件名为：作者-语录.txt

            with open(fileName, 'a+') as f:
           # f = open(fileName, 'a+')  # 追加写入文件
                f.write(text)  # 写入名言内容
                f.write('\n')  # 换行
                f.write('作者：' + autor)
                f.write('\n')  # 换行
                f.write('标签：' + tags)  # 写入标签
                f.close()  # 关闭文件操作

        next_page = response.css('li.next a::attr(href)').extract_first()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)



