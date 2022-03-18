from rest_framework import serializers
from .models import TenderModel


class TenderDetailsSerializer(serializers.ModelSerializer):
    """ Data serializer. Helps with Django model translating into JSON """

    class Meta:
        model = TenderModel
        fields = '__all__'