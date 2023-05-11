import scrapy


class ImmospiderSpider(scrapy.Spider):
    name = "immospider"
    allowed_domains = ["www.immoweb.be"]
    start_urls = ["https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&page=1&orderBy=relevance"]

    def parse(self, response):
        properties = response.css('article.card.card--result.card--xl')

        for property in properties:
            yield {
                            'name': property.css('h2 a::text').get(),
                            'url': property.css('h2 a').attrib['href']
                        }
        pass
