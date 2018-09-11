# -*- coding: utf-8 -*-
import scrapy
import requests
from bs4 import BeautifulSoup
from get_douban.items import GetDoubanItem

class GetdoubanSpider(scrapy.Spider):
    name = 'Getdouban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']
    baseurl = 'http://movie.douban.com/top250'
    def parse(self, response):
        print(response.request.headers['User-Agent'])
        data = response.body
        soup = BeautifulSoup(data, "lxml")
        items =[]
        # 找到所有的博文代码模块
        sites = soup.select('.grid_view > li')
        for site in sites:
            item = GetDoubanItem()
            # 获取图片图片地址
            item['imgurl'] =site.select('.pic > a > img')[0].get('src')
            # 查询标题
            item['title'] = site.select('.hd  > a > span')[0].get_text()
            # 查询discuss
            item['discuss'] = site.select('.bd  > .quote > .inq')[0].get_text()
            # 查询info
            info = site.select('.bd > p')[0].get_text()
            item['info'] = "".join(info.split())
            # 查询评星star
            stars = site.select('.star > span')
            item['star'] = stars[1].get_text()
            item['discussNum'] = stars[3].get_text()
            yield item
        # 调用下一页
        next_link = soup.select('.next > a')
        if next_link:
           next_link = next_link[0].get('href')
           yield scrapy.Request(self.baseurl + next_link, callback=self.parse)

