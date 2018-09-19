# 導入scrapy相關套件
import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
# 從items.py導入定義好的資料表
from book_crawler.items import BookInfoItem
# 導入urllib套件用於下載圖片
import urllib
from urllib.request import urlopen
# 將圖片encode成字串
import base64
# 導入re套件用於規格文字清理
import re
# 導入datetime套件用於判斷是否爬取該URL
from datetime import datetime


# 爬蟲
class Bookinfo_spider(scrapy.Spider):
    # 爬蟲名稱
    name = 'jap_literature'
    # 爬蟲允許爬取資料範圍
    allowed_domain = ['https://www.books.com.tw/web/sys_bbotm/books/010101']
    # 起始url，該分類第一頁
    start_urls = [
        'https://www.books.com.tw/web/sys_bbotm/books/010101/?o=1&v=1&page=1'
    ]

    # 取得該分類所有url
    def parse(self, response):
        sel = Selector(response)
        # 取得現在日期
        localtime = datetime.now().strftime('%Y-%m-%d')
        publish_time = sel.xpath(
            '//ul/li/span/text()[2]').re(r'，出版日期：(\d+-\d+-\d+)')
        link = sel.css('h4 a::attr(href)').extract()
        for pu, li in zip(publish_time, link):
            # 判斷該書出版日期是否小於現在日期，如果小於則爬取該書籍URL
            if pu < localtime:
                # 啟動爬蟲爬取當頁內容。
                yield scrapy.Request(li, callback=self.parse_bookinfo)

        # 當頁爬完後，自動換到下一頁
        # next_page_url = sel.css(".page a.nxt::attr('href')").extract()
        next_page_url = 'https://www.books.com.tw/web/sys_bbotm/books/010101/?o=1&v=1&page=2'
        yield scrapy.Request(next_page_url, callback=self.parse)
    
    # 爬取書籍相關資料
    def parse_bookinfo(self, response):
        # 將定義好的 BookInfoItem 物件指定為 bookinfo 變數
        bookinfo = BookInfoItem()   
        # 使用 scrapy 選擇器讀取 response
        sel = Selector(response)
        # 以下為將網頁中爬取到的資料加入 BookInfoItem 物件中
        bookinfo['canonical_url'] = sel.css(
            'head link:nth-child(20)::attr(href)').extract()
        bookinfo['book_name_ch'] = sel.css('h1::text').extract()
        # 抓取圖片
        image_url = sel.css(".cnt_mod002.cover_img img::attr(src)").extract()
        # 下載圖片
        image_encoded = []
        for im in image_url:
            get_image = urllib.request.urlopen('http:' + im)
            # 將圖片encode成字串
            image64 = base64.encodebytes(get_image.read())
            image_encoded.append('data:image/jpeg;base64,' + str(image64).replace("b'", '').replace("'", ''))
        bookinfo['book_image'] = image_encoded
        bookinfo['publisher'] = sel.css('span[itemprop="brand"]::text').extract()
        pub_time = sel.css(
            '.type02_p003.clearfix ul li:nth-child(3)::text').re(r'(\d+/\d+/\d+)')
        # 判斷如果出版日期結果為空則換定位下一個li排序抓取下面資料
        if len(pub_time) == 0:
            pub_time = sel.css(
                '.type02_p003.clearfix ul li:nth-child(4)::text').re(r'(\d+/\d+/\d+)')
        if len(pub_time) == 0:
            pub_time = sel.css(
                '.type02_p003.clearfix ul li:nth-child(5)::text').re(r'(\d+/\d+/\d+)')
        if len(pub_time) == 0:
            pub_time = sel.css(
                '.type02_p003.clearfix ul li:nth-child(6)::text').re(r'(\d+/\d+/\d+)')
        if len(pub_time) == 0:
            pub_time = sel.css(
                '.type02_p003.clearfix ul li:nth-child(7)::text').re(r'(\d+/\d+/\d+)')
        bookinfo['pub_time'] = pub_time
        lang = sel.css(
            '.type02_p003.clearfix ul li:nth-child(4)::text').re(r"語言：(\w*)")
        # 判斷如果語言結果為空則換定位下一個li排序抓取下面資料
        if len(lang) == 0:
            lang = sel.css(
                '.type02_p003.clearfix ul li:nth-child(5)::text').re(r"語言：(\w*)")
        if len(lang)  == 0:
            lang = sel.css(
                '.type02_p003.clearfix ul li:nth-child(6)::text').re(r"語言：(\w*)")
        if len(lang) == 0:
            lang = sel.css(
                '.type02_p003.clearfix ul li:nth-child(7)::text').re(r"語言：(\w*)")
        if len(lang) == 0:
            lang = sel.css(
                '.type02_p003.clearfix ul li:nth-child(8)::text').re(r"語言：(\w*)")
        bookinfo['lang'] = lang
        bookinfo['isbn'] = sel.css('.bd ul li:nth-child(1)::text').re(r"ISBN：(\w*)")
        bookinfo['pub_category'] = sel.css(
            'div.mod_b.type02_m058.clearfix div ul:nth-child(1) li:nth-child(2) a::text').extract()
        # 抓取規格資訊
        spec = sel.css(
            '.mod_b.type02_m058.clearfix ul:nth-child(1) li:nth-child(2)::text').re(r'規格：')
        # 判斷是否有規格欄位，如果有則爬取該欄位資料
        if '規格：' in spec:
            spec = sel.css(
                '.mod_b.type02_m058.clearfix ul:nth-child(1) li:nth-child(2)::text').extract()
            for sp in spec:
                spec_info = sp.replace(' ', '')
            bookinfo['spec'] = spec_info
        else:
            spec = sel.css(
                '.mod_b.type02_m058.clearfix ul:nth-child(1) li:nth-child(3)::text').extract()
            for sp in spec:
                spec_info = sp.replace(' ', '')
            bookinfo['spec'] = spec_info
        pub_contry = sel.css(
            '.bd ul li:nth-child(4)::text').re(r"出版地：(\w*)")
        # 判斷如果出版地結果為空則換定位上一個li排序抓取資料
        if len(pub_contry) == 0:
            pub_contry = sel.css(
                '.bd ul li:nth-child(3)::text').re(r"出版地：(\w*)")
        bookinfo['pub_contry'] = pub_contry
        bookinfo['category_first'] = sel.css(
            '.bd ul:nth-child(2) li:nth-child(1) a:nth-child(1)::text').extract()
        bookinfo['category_second'] = sel.css(
            '.bd ul:nth-child(2) li:nth-child(1) a:nth-child(2)::text').extract()
        bookinfo['category_third'] = sel.css(
            '.bd ul:nth-child(2) li:nth-child(1) a:nth-child(3)::text').extract()
        # bookinfo['content'] = sel.css('.bd div[itemprop="description"]::text').re(r'\w+\S+\n*')
        bookinfo['content'] = sel.css(
            '.bd div[itemprop="description"]::text').extract()
        bookinfo['table_of_content'] = sel.css('.bd #M201105_0_getProdTextInfo_P00a400020009_h2::text').extract()
        # 爬取作者相關資料
        bookinfo['author_ch'] = sel.css(
            '.type02_p003.clearfix ul li:nth-child(1) .trace_box ~ a::text').extract()
        author_fore = sel.css(
            '.type02_p003.clearfix ul li:nth-child(2)::text').re(r'原文作者：')
        # 判斷是否有原文作者欄位，如果有則爬取該欄位資料
        if '原文作者：' in author_fore:
            author_fore = sel.css(
                '.type02_p003.clearfix ul li:nth-child(2) a::text').extract()
            bookinfo['author_fore'] = author_fore
        else:
            bookinfo['author_fore'] = []
        bookinfo['author_fore'] = author_fore
        author_intro = sel.xpath(
                "//div[4]/div/div[3]/div[1]/div[2]/div/div[1]/strong[text()='譯者簡介']/preceding-sibling::text()").extract()
        # 判斷如果作者介紹結果為空則換從譯者簡介<b>定位抓取面上資料
        # if len(author_intro) == 0:
        #     author_intro = sel.xpath(
        #         "//div[4]/div/div[3]/div[1]/div[2]/div/div[1]/b[text()='譯者簡介']/preceding-sibling::text()").extract()
        bookinfo['author_intro'] = author_intro
        # 爬取譯者相關資料
        translator_name = sel.xpath(
                "//div[@class='mod_b type02_m057 clearfix'][2]/div/div/strong[2]/text()[3]").re(r'\n(\w+)')
        # 判斷如果譯者爬取結果為空，則改抓譯者介紹的譯者名稱
        if len(translator_name) == 0:
            translator_name = sel.css(
                '.type02_p003.clearfix ul li:nth-child(2)::text').re(r'譯者：')
            # 判斷是否有譯者欄位，如果有則爬取該欄位資料
            if '譯者：' in translator_name:
                translator_name = sel.css(
                    '.type02_p003.clearfix ul li:nth-child(2) a::text').extract()
                bookinfo['translator_name'] = translator_name
            else:
                # 如果沒有則爬取下面一個欄位
                translator_name = sel.css(
                    '.type02_p003.clearfix ul li:nth-child(3) a::text').extract()
                bookinfo['translator_name'] = translator_name
        else:
            bookinfo['translator_name'] = translator_name
        translator_intro = sel.xpath(
            "//div[4]/div/div[3]/div[1]/div[2]/div/div[1]/strong[text()='譯者簡介']/following-sibling::text()").extract()
        # 判斷如果譯者介紹結果為空則換從譯者名稱<b>定位抓取下面資料
        # if len(translator_intro) == 0:
        #     translator_intro = sel.xpath(
        #         "//div[4]/div/div[3]/div[1]/div[2]/div/div[1]/b[text()='譯者簡介']/following-sibling::text()").extract()
        #     bookinfo['translator_intro'] = translator_intro
        bookinfo['translator_intro'] = translator_intro
        # 返回書籍list
        yield bookinfo
