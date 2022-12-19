import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from sourceChannel import webCrawler
 

process = CrawlerProcess()
process.crawl(webCrawler.BlogSpider, category="electronics")
process.start();