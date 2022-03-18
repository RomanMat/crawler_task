from rest_framework import generics
from .serializers import TenderDetailsSerializer
from .models import TenderModel
from rest_framework.permissions import IsAuthenticated 

# API view
class TenderListView(generics.ListAPIView):
    """ Represent full list of tenders """

    permission_classes = (IsAuthenticated,)  
    serializer_class = TenderDetailsSerializer
    queryset = TenderModel.objects.all()

# API view
class TenderSearchView(generics.ListAPIView):
    """ View class, that helps to retrieve data by inputed date """

    permission_classes = (IsAuthenticated,)  
    serializer_class = TenderDetailsSerializer
    lookup_url_kwarg = "date"

    
    def get_queryset(self):
        """ By date results fetching """

        date = self.kwargs.get(self.lookup_url_kwarg)
        return TenderModel.objects.filter(date=date)

# API view
class TenderIdView(generics.RetrieveAPIView):
    """ View class for getting single data-items by pk """

    permission_classes = (IsAuthenticated,)  
    serializer_class = TenderDetailsSerializer
    queryset = TenderModel.objects.all()



