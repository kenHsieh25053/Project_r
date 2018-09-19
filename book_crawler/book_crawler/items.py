# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 定義書籍資料表
class BookInfoItem(scrapy.Item):
    # define the fields for your item here like:
    canonical_url = scrapy.Field()
    book_name_ch = scrapy.Field()
    book_name_fore = scrapy.Field()
    book_image = scrapy.Field()
    publisher = scrapy.Field()
    pub_time = scrapy.Field()
    lang = scrapy.Field()
    isbn = scrapy.Field()
    pub_category = scrapy.Field()
    spec = scrapy.Field()
    pub_contry = scrapy.Field()
    category_first = scrapy.Field()
    category_second = scrapy.Field()
    category_third = scrapy.Field()
    content = scrapy.Field()
    table_of_content = scrapy.Field()
    author_ch = scrapy.Field()
    author_fore = scrapy.Field()
    author_intro = scrapy.Field()
    translator_name = scrapy.Field()
    translator_intro = scrapy.Field()


