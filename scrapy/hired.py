import scrapy

class Getajob(scrapy.Spider):
	name = 'I need a Job'
	start_urls = [
		'http://queroworkar.com.br/blog/vagas/'
	]

	custom_settings = {
		'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36'
	}

	def parse(self, response):
		#company = response.xpath("//div/div/span[@class='jobs-author']").extract()
		title 	= response.xpath("//div/div/div/div/h4/a/text()").extract() 
		yield{'empresa':title}

		next_selector = '.link-button ::attr(href)'
		next_page 	  = response.css(next_selector).extract_first()

		if next_page:
			yield scrapy.Request(
				response.urljoin(next_page),
				callback = self.parse
			) 