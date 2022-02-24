# import requests library
import requests
#import scrapy to run scrapy code below

# Target url
url = "https://brickset.com/sets/year-2011"
r = requests.get(url)


# Getting the headers of the target website
h = requests.head(url)
print(url)
print("Website Header:")
print("****")
print("Status code:")
print("\t *", r.status_code, "OK")

# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("****")



import scrapy

class NewSpider(scrapy.Spider):
   name = "new_spider"
   start_urls = ["https://brickset.com/sets/year-2011"]

   def parse(self, response):
      css_selector = 'img'
      for x in response.css(css_selector):
         newsel = '@src'
         yield {
                 'Image Link': x.xpath(newsel).extract_first(),
         }
