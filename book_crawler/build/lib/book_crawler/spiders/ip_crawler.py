# 導入scrapy相關套件
import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.conf import settings


# 爬蟲
class Ip_spider(scrapy.Spider):
    # 爬蟲名稱
    name = 'ip_crawler'
    # 爬蟲允許爬取資料範圍
    allowed_domain = [
        # 'https://hidemyna.me/en/proxy-list/'
        'https://www.us-proxy.org/'
    ]
    # 起始url，該分類第一頁
    start_urls = [
        'https://www.us-proxy.org/'
        # 'https://hidemyna.me/en/proxy-list/#list'
    ]

    # 取得所有IP和port號
    def parse(self, response):
        sel = Selector(response)
        # 指定檔案路徑(從settings.py讀取)
        file = settings.get('PROXY_LIST')
        # 爬取IP和port號
        ip_address = sel.xpath(
            '/*[@id="proxylisttable"]/tbody/tr[1]/td[1]/text()').extract()
        port = sel.xpath(
            '/*[@id="proxylisttable"]/tbody/tr[1]/td[2]/text()').extract()
        print(ip_address)
        # 將IP和port號寫入proxy.txt檔
        for i, p in zip(ip_address, port):
            with open(file) as f:
                f.write('{0}:{1}'.format(i, p))
        # 當頁爬完後，自動換到下一頁
        # next_page_url = sel.css(
        #     "#proxylisttable_next a::attr('href')").extract()
        # next_page_url = 'https://hidemyna.me/en/proxy-list/?start=64#list'
        # yield scrapy.Request(next_page_url, callback=self.parse)

