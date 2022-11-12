import scrapy


class ProductItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    originalPrice = scrapy.Field()
    ratingAverageProduct = scrapy.Field()
    discount = scrapy.Field()
    thumbnailUrl = scrapy.Field()
    description = scrapy.Field()
    imagesProduct = scrapy.Field()
    optionsType = scrapy.Field()
    optionsProduct = scrapy.Field()
