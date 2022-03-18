from ..items import TenderItem


import scrapy
import json
import datetime

class TenderSpider(scrapy.Spider):
    """ Scrapy spider-class, that desdribe used headers, js-body params. 
    Also you can find how scraping works in 'parse' function """

    # Scrapy enviroment variables
    name = 'tender'
    allowed_domains = ['www.e-licitatie.ro']
    start_urls = ['http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1']

    # Defines how much items will be shown at one request
    PAGE_SIZE = 1

    # Headers for request
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language':' uk-UA,uk;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Culture': 'en-US',
            'Authorization': 'Bearer null',
            'RefreshToken': 'null',
            'HttpSessionID': 'C9E6B45F-4049-42FE-B184-80B2A9EB2694',
            'Content-Type': 'application/json;charset=utf-8',
            'Origin': 'http://www.e-licitatie.ro',
            'Connection': 'keep-alive',
            'Referer': 'http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1',
        }

    # We will make POST requests so it will be them body
    params = {'sysNoticeTypeIds': '[]',
        'endPublicationDate': f'{datetime.date.today()}',
        'sortProperties': '[]',
        'pageSize': f'{PAGE_SIZE}',
        'hasUnansweredQuestions': 'false',
        'pageIndex': '0',
        'startPublicationDate': f'{datetime.date.today()}',
    }

    def start_requests(self):
        """ Actually stuff that will happen firstly (request with deligated params) """

        yield scrapy.Request(url='http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/', 
        method='POST', callback=self.parse, 
        headers=self.headers, body=json.dumps(self.params))

    def parse(self, response):
        """ Requested data converts into items and is requesting more times untill all data will be fetched """

        # Transforming into item
        data = json.loads(response.body)
        items_list = data['items']
        item = TenderItem()
        
        # Sorting all data by keys and sending to pipelines
        for items in items_list:
            item['date'] = items['noticeStateDate']
            item['notice_number'] = items['noticeNo']
            item['tender_name'] = items['contractTitle']
            item['procedure_state'] = items['sysProcedureState']['text']
            item['contract_type'] = items['sysAcquisitionContractType']['text']
            if items['isOnline']: item['procurement_type'] = 'ONLINE'
            else: item['procurement_type'] = 'OFFLINE'
            item['estimated_value'] = items['estimatedValueExport']
            yield item

        # Repeat request data if there is unfetched data
        if data['total'] > self.PAGE_SIZE and int(self.params['pageIndex']) < int(data['total']) / self.PAGE_SIZE:
            self.params['pageIndex'] = str(int(self.params['pageIndex']) + 1)

            yield scrapy.Request(url='http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/', 
            method='POST', callback=self.parse, 
            headers = self.headers, body=json.dumps(self.params))



