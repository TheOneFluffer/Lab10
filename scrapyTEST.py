import scrapy
from scrapy.http.request import Request

class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://brickset.com/sets/year-2019']

    #def start_requests(self):
     #   headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
      #  for url in self.start_urls:
       #     yield Request(url, headers=headers)

    #def parse(self, response):
     #   css_selector = 'img'
      #  for x in response.css(css_selector):
        #    newsel = '@src'
       #     yield {
         #       'Image Link': x.xpath(newsel).extract_first(),
         #   }

    def parse(self, response):
        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }

#To recurse to next page
Page_selector = '.next a ::attr(href)'
next_page = response.css(Page_selector).extract_first()
if next_page:
    yield scrapy.Request(
        response.urljoin(next_page),
        callback=self.parse
    )
