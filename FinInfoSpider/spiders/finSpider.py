import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup
from FinInfoSpider.items import FininfospiderItem
# 从另一个网站爬取股票代码应对表
from FinInfoSpider.spiders.CodeParse import getStockCode
import json



class myspider(scrapy.Spider):

    name = 'fin_info'
    # allowed_domains = ['stockpage.10jqka.com.cn']
    start_urls = ['http://basic.10jqka.com.cn/', '/finance.html#stockpage']
    parse_id = getStockCode().get()


    def start_requests(self):
        send_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8"}

        for id in self.parse_id:
            url = self.start_urls[0] + id + self.start_urls[1]
            yield Request(url, headers=send_headers, callback=self.parse)

    def parse(self, response):
        # parse中切记一定要用yield否则会直接结束程序
        response = BeautifulSoup(response.text, 'lxml')
        name = response.find('input', id='stockName')['value']

        # 对港股和个股的不同情况作出分别应对
        json_data = response.find('p', id='main')
        if json_data:
            pass
        else:
            json_data = response.find('p', id='keyindex')
        yield self.get_items(json_data, name)

    def get_items(self,json_data, name):
        item = FininfospiderItem()
        info = json.loads(json_data.text)
        title = info['title']
        years = info['report'][0]
        # 拼接标题列表
        titles = []
        for num in range(1, len(info['title'])):
            titles.append(title[num][0])
        # 拼接数据集
        data_set = []
        for i in range(0, len(years)):
            data = []
            for j in info['report']:
                # 剔除数据中的空项
                if j[i]=='':
                    data.append('--')
                elif j[i]==False:
                    data.append('--')
                else:
                    data.append(j[i])
            data_set.append(data)
        item['data_set'] = data_set
        item['titles'] = titles
        item['name'] = name

        return item

