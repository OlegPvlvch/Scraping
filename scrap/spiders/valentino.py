from scrapy_redis.spiders import RedisSpider
import scrapy
from scrap.items import ProductItem

class ValentinoSpider(RedisSpider):
    name = 'valentino'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/5'
    }

    #start_urls = ["https://www.valentino.com/en-us/men/bags"]

    def parse(self, response):
        links = response.xpath(
            "//section[contains(@id, 'wrapper-product-lists')]/ul[contains(@class, 'products__list')]/li/a/@href"
        ).extract()
        category = response.xpath(
            "//span[contains(@class, 'searchresult__title')]/h1/text()"
        ).extract_first()
        for url in links:
            yield scrapy.Request(url=url, 
                                callback=self.parse_product,
                                meta={
                                    'category':category
                                })
    
    def parse_product(self, response):
        item = ProductItem()
        #category, price, title, colors, sizes, images, description
        item['category'] = response.meta['category']
        item['price'] = response.xpath(
            "//div[contains(@class, 'price')]//span[contains(@class, 'value')]/text()").extract_first()
        item['title'] = response.xpath(
            "//span[contains(@class, 'modelName')]/text()").extract_first()
        item['colors'] = response.xpath(
            "//span[contains(@class, 'selectedColorInfo')]/text()").extract()
        item['sizes'] = response.xpath(
            "//span[contains(@class, 'sizeLabel')]/text()").extract()
        item['images'] = response.xpath(
            "//div[contains(@class, 'alternativeProductShots')]/ul/li/img/@src").extract()
        item['description'] = response.xpath(
            "//div[contains(@class, 'itemInfo-itemDescription')]/p/span[contains(@class, 'value')]/text()"
        ).extract()

        return item

    