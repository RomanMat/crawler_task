from django.urls import path, register_converter
from datetime import datetime
from .views import TenderIdView, TenderListView, TenderSearchView

class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value

register_converter(DateConverter, 'yyyy')

urlpatterns = [
    path('list/', TenderListView.as_view(), name='tenders_list'),
    path('search/<yyyy:date>/', TenderSearchView.as_view(), name='search_tender'),
    path('<int:pk>/', TenderIdView.as_view(), name='tender_by_pk'),
]