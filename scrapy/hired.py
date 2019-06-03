import scrapy

class Getajob(scrapy.Spider):
	name = 'I need a Job'
	start_urls = [
		'http://queroworkar.com.br/blog/jobs/',
		#'https://www.indeed.com.br/empregos-de-programador-em-Fortaleza'
	]

	custom_settings = {
		'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36'
	}

	def parse(self, response):
		title 	= response.xpath("//div/article/div/div/h2[@class='loop-item-title']/a/text()").extract()
		company = response.xpath("//div/article/div/div/p/span[@class='job-company']/a/span/text()").extract() 
		
		yield{
		'company': company,
		'title': title
		}
		
		
		next_selector = '.next.page-numbers ::attr(href)'
		next_page 	  = response.css(next_selector).extract_first()

		if next_page:
			yield scrapy.Request(
				response.urljoin(next_page),
				callback = self.parse
			) 

