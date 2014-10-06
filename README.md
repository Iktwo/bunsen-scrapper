bunsen-scrapper
===============

Scrapy project to scrap bunsen comics

Generate the model:

	scrapy crawl bunsen -o model.json

Test scrapy:

	scrapy shell http://www.bunsencomics.com/?category=Bunsen+C%C3%B3mics
	response.body
	response.xpath('//article').xpath('h1/a[contains(text(), "Bunsen")]/text()')

