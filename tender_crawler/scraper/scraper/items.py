from scrapy_djangoitem import DjangoItem
from romanian_tender.models import TenderModel

class TenderItem(DjangoItem): 
   """ Scrapy class that converts Django model into scrapy item """
   
   django_model = TenderModel
