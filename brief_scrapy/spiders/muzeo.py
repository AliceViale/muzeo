import scrapy

from brief_scrapy.items import BriefScrapyItem


class MuzeoSpider(scrapy.Spider):
    name = 'muzeo'
    allowed_domains = ['web']
    start_urls = ['https://fr.muzeo.com/papier-peint-oeuvre/nighthawks/edward-hopper#Nighthawks-Edward-Hopper']

    def parse(self, response):
        item=BriefScrapyItem()
        item['title']=response.xpath('/html/body/div[1]/div[3]/div/div[3]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div/div[1]/h1/span[2]/text()').extract()
        return item


