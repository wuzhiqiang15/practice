import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes_02'
    start_urls = ['http://quotes.toscrape.com/tag/humor/', ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield{
                'text': quote.css("span.text::text").extract_first(),
                "author": quote.xpath("span/small/text()").extract_first(),
            }

        next_paeg = response.css("li.next a::attr('href')").extract_first()
        if next_paeg is not None:
            yield response.follow(next_paeg, self.parse)

