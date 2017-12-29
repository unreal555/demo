#!/bin/py
#   -*-coding:utf-8-*-
#!/bin/py
#   -*-coding:utf-8-*-
import requests
from lxml import etree
agent = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'

# headers = {'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8',
#            'Accept-Encoding': 'gzip, deflate, sdch',
#            'Accept-Language': 'zh-CN,zh;q=0.8',
#            'Cache-Control': 'max-age=0',
#            'Connection': 'keep-alive',
#            'Host': 'www.lagou.com',
#            'User_Agent': agent,
#            'Upgrade-Insecure-Requests': '1',
#            'Referer':'www.lagou.com'}
headers={
        'User-Agent':agent
         }
# cookie = {
#             'user_trace_token': '20171227135143-047f5eea-eaca-11e7-9eaf-5254005c3644',
#             'LGUID': '20171227135143-047f627c-eaca-11e7-9eaf-5254005c3644',
#             'index_location_city': '%E5%85%A8%E5%9B%BD',
#             'JSESSIONID': 'ABAAABAABEEAAJA090E4F5AFF317904401AB226993FCC6A',
#             'TG-TRACK-CODE': 'index_navigation',
#             'SEARCH_ID': '9a9a56cf257d4d8fb70c32ac59f96d00',
#             '_gid': 'GA1.2.1701888003.1514353912',
#             'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1514353913,1514421854',
#             'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1514429505',
#             '_ga': 'GA1.2.2079792536.1514353912',
#             'LGSID': '20171228120907-d94b89f2-eb84-11e7-9ebb-5254005c3644',
#             'PRE_UTM': '',
#             'PRE_HOST': 'www.baidu.com',
#             'PRE_SITE': 'www.baidu.com',
#             'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F',
#             'LGRID': '20171228120907-d94b8c5f-eb84-11e7-9ebb-5254005c3644'
#             }
sess=requests.session()
sess.get('https://www.lagou.com')
response=sess.get("https://www.lagou.com/zhaopin/rongzi/2",headers=headers)
#response.encoding=('gbk')
#print(response.content.decode('utf-8'))
root=etree.HTML(response.content.decode("utf-8"))

for i in root.xpath('//*[@id="s_position_list"]/ul/li/div/div/div/a'):

    print(i.xpath('./@href'))


