"""tender_crawler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Admin panel url
    path('admin/', admin.site.urls),

    # API urls
    path('api/v1/tenders/', include('romanian_tender.urls'), name='base_endpoint'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
