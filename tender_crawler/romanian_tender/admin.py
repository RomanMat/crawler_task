from django.contrib import admin
from .models import TenderModel
from django.contrib.auth.models import Group

admin.site.register(TenderModel)

admin.site.unregister(Group)