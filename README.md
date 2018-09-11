# python3-Getdouban
scrapy爬虫  Mongo存储  BeautifulSoup 抓取网页标签


使用方法  
1. git clone git@github.com:guogj/python3-Getdouban.git

2. 进入get_douban目录
cd python3-Getdouban/get_douban

3.执行
 scrapy crawl Getdouban --nolog
 
爬取生产json文件
scrapy crawl  Getdouban  -o test.json

保存csv文件
scrapy crawl Getdouban  -o test.csv
