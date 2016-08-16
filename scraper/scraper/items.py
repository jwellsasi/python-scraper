# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class MetaItem(Item):
	url = Field()
	#productBrand = Field()
	#FurnitureStore = Field()
	#storeName = Field()
	#streetAddress = Field()
	#addressLocality = Field()
	#addressRegion = Field()
	#imgalt = Field()
	#urlstatus = Field()
	title = Field()
	description = Field()  	
	canonical = Field()
	#numresults = Field()
	#relprev = Field()
	#relnext = Field()		
	#h1 = Field()
	#h2 = Field()
	#h3 = Field()
	#h4 = Field()
	#h5 = Field()
	#h6 = Field() 
	#itempropprice = Field()
	#hawkbannertop = Field()
	#hawkcustomhtml = Field()	
	referrer = Field()