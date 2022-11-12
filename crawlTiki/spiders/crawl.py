import scrapy
from scrapy_splash import SplashRequest
from scrapy.exceptions import CloseSpider

import re

from crawlTiki.items import ProductItem
from crawlTiki.helper.TikiHelperHandleDataProduct import TikiHelperHandleDataProduct
from crawlTiki.dto.ObjectDTO import ImageDTO
from crawlTiki.constant.constant import API_DETAIL_URL
from crawlTiki.helper.TikiHelperUtil import TikiHelperUtil


class CrawlCategoriesSpider(scrapy.Spider):
    name = 'dataTiki'
    allowed_domains = ['tiki.vn']
    start_urls = ['https://tiki.vn/']

    def __init__(self, *args, **kwargs):
        super(CrawlCategoriesSpider, self).__init__(*args, **kwargs)
        self.limitProduct: int = int(kwargs.get('limitProduct', None))
        self.pathName: str = kwargs.get('pathName', None)
        self.typeImage: str = kwargs.get('typeImage', None)
        self.keyWord: str = kwargs.get('keyWord', None)
        self.counter: int = 1
        self.tikiHelperUtil = TikiHelperUtil()

    render_script = """
        function main(splash)
            local url = splash.args.url
            assert(splash:go(url))
            assert(splash:wait(5))

            return {
                html = splash:html(),
                url = splash:url(),
            }
        end
     """

    def start_requests(self):

        listUrl: list[str] = self.tikiHelperUtil.handle_url(
            self.keyWord, self.limitProduct)

        for url in listUrl:
            yield SplashRequest(
                url,
                self.parse_list_product,
                endpoint='render.html',
                args={
                    'wait': 5,
                    'lua_source': self.render_script,
                },
            )

    def parse_list_product(self, response):
        if response.status == 404:
            raise CloseSpider('Receive 404 response')

        listProducts: list[str] = response.css(".product-item")
        if (listProducts == []):
            raise CloseSpider('Error selector list products')

        for product in listProducts:
            if self.counter > self.limitProduct:
                break

            self.counter += 1
            productLink = product.css("a::attr(href)").extract()
            temp = re.search('\d{6,10}', str(productLink))
            productID = temp.group()

            url = f'{API_DETAIL_URL}{productID}'
            yield response.follow(url=url, callback=self.parse_product_info)

    def parse_product_info(self, response):
        if response.status == 404:
            raise CloseSpider('Receive 404 response')
        try:
            item = ProductItem()
            modelOptionsImage: ImageDTO = ImageDTO(
                self.pathName, self.typeImage)
            tikiHelperHandleDataProduct = TikiHelperHandleDataProduct(
                response.text, modelOptionsImage)
            dataProductInfo = tikiHelperHandleDataProduct.handle_Product()
                        
            item["name"] = dataProductInfo.name
            item["price"] = dataProductInfo.price
            item["originalPrice"] = dataProductInfo.originalPrice
            item["ratingAverageProduct"] = dataProductInfo.ratingAverageProduct
            item["thumbnailUrl"] = dataProductInfo.thumbnailUrl
            item["description"] = dataProductInfo.description
            item["imagesProduct"] = dataProductInfo.imagesProduct
            item["optionsType"] = dataProductInfo.optionsType
            item["optionsProduct"] = dataProductInfo.optionsProduct
            yield item
        except BaseException as e:
            raise CloseSpider(e)
