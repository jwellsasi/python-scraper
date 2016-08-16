# -*- coding: utf-8 -*-
'''
To run this crawl and output to csv
scrapy crawl sitemap-scraper -o domain-com-xmlcrawl-3-14-16.csv
command has to be run from the /scraper/scraper/ path and not inside the /spider folder
'''
import scrapy
from scrapy.spiders import SitemapSpider
from scrapy.selector import Selector
from scraper.items import MetaItem

class SitemapScraperSpider(SitemapSpider):
    name = "sitemap-scraper"
    sitemap_urls = ['http://www.domain.com/sitemap.xml']
    sitemap_rules = [
        ('', 'parse_item'),
    ]

    def parse_item(self, response):

        sel = Selector(response)
        sites = sel.xpath('//html')
        items = []

        for site in sites:
            item = MetaItem()
            item['url'] = response.url
            #item['urlstatus'] = response.status
            #item['title'] = site.xpath('//title/text()').extract()
            #item['description'] = site.xpath("//meta[@name='description']/@content").extract()
            #item['canonical'] = site.xpath("//link[@rel='canonical']/@href").extract()
            #item['h1'] = site.xpath("//h1/text()").extract()
            #item['h2'] = site.xpath("//h2/text()").extract()
            #item['h3'] = site.xpath("//h3/text()").extract()
            #item['h4'] = site.xpath("//h4/text()").extract()
            #item['h5'] = site.xpath("//h5/text()").extract()                                                
            #item['h6'] = site.xpath("//h6/text()").extract()   
            item['referrer'] = response.request.headers.get('Referer', None)         
            items.append(item)
        return items