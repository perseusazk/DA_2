# import library
import unittest

import requests
import scrapy

#import scrapy to run scrapy code below
url = "https://brickset.com/sets/year-2011"
# Target url
r = requests.get(url)
print("Status code:")
print("\t *", r.status_code, "OK")

# Getting the headers of the target website
h = requests.head(url)
print(url)
print("Website Header:")
print("****")


# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("****")

#to enable unittest
class TestCase(unittest.TestCase):
    def testExample(self):
        print("")















class NewSpider(scrapy.Spider):
   name = "new_spider"
   start_urls = ['http://brickset.com/sets/year-2011']
   def parse(self, response):
      xpath_selector = '//img'
      for x in response.xpath(xpath_selector):
         newsel = '@src'
         yield {
            'Image Link': x.xpath(newsel).extract_first(),
         }
# To recurse next page
      Page_selector = '.next a ::attr(href)'
      next_page = response.css(Page_selector).extract_first()
      if next_page:
         yield scrapy.Request(
            response.urljoin(next_page),
            callback=self.parse
      )

if __name__ == "__main__":
    unittest.main()