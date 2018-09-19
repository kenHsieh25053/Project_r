# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import random

from urllib.parse import urlparse
from scrapy.http import Request
from scrapy.utils.python import WeakKeyCache
from scrapy.conf import settings


# 設置隨機User agent模擬瀏覽器行為
class MyUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent):
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user_agent=crawler.settings.get('MY_USER_AGENT')
        )

    def process_start_requests(self, request, spider):
        agent = random.choice(self.user_agent)
        request.headers['User-Agent'] = agent

# 設置代理伺服器並隨機挑選IP使用
# class ProxyMiddleware(object):
#     def __init__(self):
#         self.proxy_list = settings.get('PROXY_LIST')
#         with open(self.proxy_list, "r", encoding="utf-8", errors='ignore') as f:
#             self.proxies = [ip.strip() for ip in f]
    
#     def process_request(self, request, spider):
#         request.meta['proxy'] = 'http://{}'.format(random.choice(self.proxies))


# 使用 google 快取訪問網頁
class GoogleCacheMiddleware(object):
    """
        this middleware allow spider to crawl the spicific domain url in google caches.
        you can define the GOOGLE_CACHE_DOMAINS in settings,it is a list which you want to visit the 
        google cache.Or you can define a google_cache_domains in your spider and it is as the highest 
        priority.
    """
    google_cache = 'http://webcache.googleusercontent.com/search?q=cache:'

    def __init__(self, cache_domains=''):
        self.cache = WeakKeyCache(self._cache_domains)
        self.cache_domains = cache_domains

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings['GOOGLE_CACHE_DOMAINS'])

    def _cache_domains(self, spider):
        if hasattr(spider, 'google_cache_domains'):
            return spider.google_cache_domains
        elif self.cache_domains:
            return self.cache_domains

        return ""

    def process_request(self, request, spider):
        """
            the scrapy documention said that:
                "If it returns a Request object, the returned request will be rescheduled (in the Scheduler)
                to be downloaded in the future. The callback of the original request will always be called. 
                If the new request has a callback it will be called with the response downloaded, and the 
                output of that callback will then be passed to the original callback. If the new request doesn’t
                have a callback, the response downloaded will be just passed to the original request callback."
             but actually is that if it returns a Request object,then the original request will be droped,so 
             you must make sure that the new request object's callback is the original callback.
        """
        gcd = self.cache[spider]
        if gcd:
            if urlparse(request.url).netloc in gcd:
                request = request.replace(url=self.google_cache + request.url)
                request.meta['google_cache'] = True
                return request

    def process_response(self, request, response, spider):

        if request.meta.get('google_cache', False):
            return response.replace(url=response.url[len(self.google_cache):])

        return response

# class BookCrawlerSpiderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.

#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s

#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.

#         # Should return None or raise an exception.
#         return None

#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.

#         # Must return an iterable of Request, dict or Item objects.
#         for i in result:
#             yield i

#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.

#         # Should return either None or an iterable of Response, dict
#         # or Item objects.
#         pass

#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.

#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r

#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
