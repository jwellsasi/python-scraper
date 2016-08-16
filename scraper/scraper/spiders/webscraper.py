# -*- coding: utf-8 -*-
'''
To run this crawl and output to csv
scrapy crawl webscraper -o www-domain-8-15-16.csv
command has to be run from the /scraper/scraper/ path and not inside the /spider folder
'''
import scrapy
from scrapy.spiders import CrawlSpider, Rule
# Use this following import to identify and filter external links
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scraper.items import MetaItem

class WebscraperSpider(CrawlSpider):
    name = "webscraper"
    allowed_domains = ["domain.com"] 
    start_urls = ['http://domain.com']

    rules = (
        # Extract links matching allow='' and deny those in deny='' parse in method parse_item
        Rule(LinkExtractor(allow=('.*', ), deny=('\?', )), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=('', ), deny=('', )), callback='parse_item', follow=True),        
    )

    def parse_item(self, response):

        sel = Selector(response)
        sites = sel.xpath('//html')
        items = []

        for site in sites:
            item = MetaItem()
            item['url'] = response.url
            #item['productBrand'] = site.xpath("//h1[@class='subtitle']/span[@class='text-smaller']").extract()
            #item['storeName'] = site.xpath("//h1[@itemprop='name']/text()").extract()[0].strip()
            #item['streetAddress'] = site.xpath("//span[@itemprop='streetAddress']/text()").extract()[0].strip()
            #item['addressLocality'] = site.xpath("//span[@itemprop='addressLocality']/text()").extract()[0].strip()
            #item['addressRegion'] = site.xpath("//span[@itemprop='addressRegion']/text()").extract()[0].strip()
            #item['FurnitureStore'] = site.xpath("//div[@itemtype='http://schema.org/FurnitureStore']").extract()
            #item['imgalt'] = site.xpath('//img/@alt').extract()
            #item['urlstatus'] = response.status
            item['title'] = site.xpath('//title/text()').extract()
            item['description'] = site.xpath("//meta[@name='description']/@content").extract()
            item['canonical'] = site.xpath("//link[@rel='canonical']/@href").extract()
            #item['numresults'] = site.xpath("//div[@class='search-navigation-page-number text-small']/text()").extract()
            #item['relprev'] = site.xpath("//link[@rel='prev']/@href").extract()
            #item['relnext'] = site.xpath("//link[@rel='next']/@href").extract()
            #item['h1'] = site.xpath("//h1/text()").extract()
            #item['h2'] = site.xpath("//h2/text()").extract()
            #item['h3'] = site.xpath("//h3/text()").extract()
            #item['h4'] = site.xpath("//h4/text()").extract()
            #item['h5'] = site.xpath("//h5/text()").extract()                                                
            #item['h6'] = site.xpath("//h6/text()").extract()  
            #item["itempropprice"] = site.xpath("//span[@itemprop='price']/@content").extract() 
            #item["hawkbannertop"] = site.xpath("//div[@id='hawkbannertop']").extract()
            item['referrer'] = response.request.headers.get('Referer', None)  
            #item['hawkcustomhtml'] = site.xpath("//div[@id='hawkcustomhtml']").extract()    
            items.append(item)
        return items