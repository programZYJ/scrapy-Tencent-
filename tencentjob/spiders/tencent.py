# -*- coding: utf-8 -*-
import scrapy
from tencentjob.items import TencentjobItem
import re
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
# class TencentSpider(scrapy.Spider):
class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    page_lx = LinkExtractor(allow=("start=\d+"))
    rules = [Rule(page_lx,callback="parseContent", follow=True)]
    # def parse(self, response):
    def parseContent(self, response):
        # open("job.html","wb").write(response.body)
        for each in response.xpath('//*[@class="even"]'):
            items = TencentjobItem()
            name = each.xpath('./td[1]/a/text()').extract()
            detailLink = each.xpath('./td[1]/a/@href').extract()
            positionInfo = each.xpath('./td[2]/text()').extract()
            peopleNumber = each.xpath('./td[3]/text()').extract()
            workLocation = each.xpath('./td[4]/text()').extract()
            publishTime = each.xpath('./td[5]/text()').extract()
            items['name'] = name[0]
            items['detailLink'] = detailLink[0]
            items['positionInfo'] = positionInfo[0]
            items['peopleNumber'] = peopleNumber[0]
            items['workLocation'] = workLocation[0]
            items['publishTime'] = publishTime[0]
            # curpage = re.search('(\d+)', response.url).group(1)
            # page = int(curpage) + 10
            # url = re.sub('\d+', str(page), response.url) + "#a"
            # yield scrapy.Request(url, callback=self.parse)
            yield items
