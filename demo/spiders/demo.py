#!/bin/py
#   -*-coding:utf-8-*-
import scrapy
import random
from demo.useragent import agents
from demo.items import WorkInfo

agent = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'


# User-Agent:Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36


class demo(scrapy.Spider):
    headers = {
        'User-Agent': agent
    }
    # cookie = {
    #     'user_trace_token': '20171227135143-047f5eea-eaca-11e7-9eaf-5254005c3644',
    #     'LGUID': '20171227135143-047f627c-eaca-11e7-9eaf-5254005c3644',
    #     'index_location_city': '%E5%85%A8%E5%9B%BD',
    #     'JSESSIONID': 'ABAAABAABEEAAJA090E4F5AFF317904401AB226993FCC6A',
    #     'TG-TRACK-CODE': 'index_navigation',
    #     'SEARCH_ID': '9a9a56cf257d4d8fb70c32ac59f96d00',
    #     '_gid': 'GA1.2.1701888003.1514353912',
    #     'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1514353913,1514421854',
    #     'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1514429505',
    #     '_ga': 'GA1.2.2079792536.1514353912',
    #     'LGSID': '20171228120907-d94b89f2-eb84-11e7-9ebb-5254005c3644',
    #     'PRE_UTM': '',
    #     'PRE_HOST': '',
    #     'PRE_SITE': '',
    #     'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F',
    #     'LGRID': '20171228120907-d94b8c5f-eb84-11e7-9ebb-5254005c3644'
    # }

    name = 'demo'
  #  allowed_domains = 'www.lagou.com'
    start_urls = ['https://www.lagou.com']

    # session=requests.session()
    # response = session.get("http://www.lagou.com")
    # response.encoding = ('utf-8')
    def parse(self, response):

        for i in response.xpath('//*[@class="menu_box"]/div/div/a'):
            work = i.xpath('text()').extract()
            url = i.xpath('@href').extract()

            info = WorkInfo()
            info['work'] = work
            info['url'] = url

            # try:
            #     print(info['url'], info['work'])
            #     yield scrapy.Request(url=url[0] + '1',  headers=self.headers,
            #                          meta={"work": work}, callback=self.parse_url)
            #     break
            #
            # except :
            #     print("xxx")
            #     pass
            yield scrapy.Request(url=url[0] + '1',  headers=self.headers,
                                                          meta={"work": work}, callback=self.parse_url)
            break

    def parse_url(self, response):
        print(response.body)
        work = response.meta["work"]

        # print(title)
        for sel2 in response.xpath('//ul[@class="item_con_list"]/li'):
            url=sel2.xpath('div/div/div/a').xpath('@href').extract()
            work = sel2.xpath('div/div/div/a/h3/text()').extract()
            jobPlace = sel2.xpath('div/div/div/a/span/em/text()').extract()
            jobMoney = sel2.xpath('div/div/div/div/span/text()').extract()
            jobNeed = sel2.xpath('div/div/div/div/text()').extract()
            jobNeed = jobNeed[2].strip()
            jobCompany = sel2.xpath('div/div/div/a/text()').extract()
            jobCompany = jobCompany[3].strip()

            jobType = sel2.xpath('div/div/div/text()').extract()
            jobType = jobType[7].strip()

            jobSpesk = sel2.xpath('div[@class="list_item_bot"]/div/text()').extract()
            jobSpesk = jobSpesk[-1].strip()

            Item = WorkInfo()
            Item["work"] = work
            Item["jobPlace"] = jobPlace
            Item["jobMoney"] = jobMoney
            Item["jobNeed"] = jobNeed
            Item["jobCompany"] = jobCompany
            Item["jobType"] = jobType

            Item["jobSpesk"] = jobSpesk
            # print(url)
            Item["jobUrl"]=url[0]
            Item["gongsiUrl"]=url[1]
            yield Item
