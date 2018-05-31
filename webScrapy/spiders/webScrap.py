import scrapy

class JobSpider(scrapy.Spider):
    name = "Jobs"
    start_urls = [
        'https://www.indeed.com/jobs?q=permit+expeditor&l='
    ]

    def parse(self, response):
        print(response.url)
        a_selectors = response.xpath("//a")
        for selector in a_selectors:
            text = selector.xpath("text()").extract_first()
            link = selector.xpath("@href").extract_first()
            request = response.follow(link, callback=self.parse)
            if text == 'permit expeditor':
                print text
            yield request

x