import scrapy
import json

class QuotesscrappingSpider(scrapy.Spider):
	name = 'project'
	quotes_base_url = 'http://quotes.toscrape.com/api/quotes?page=%s'
	start_urls = [quotes_base_url % 1]
	download_delay = 1.5
	
	def parse(self, response):	
		json_data = json.loads(response.text)
		for quote in json_data['quotes']:
			yield quote
		if json_data('has_next'):
			yield scrapy.Request(self.quotes_base_url % (int(json_data['page']) + 1))