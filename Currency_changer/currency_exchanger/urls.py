from django.contrib import admin
from django.urls import path
from .views import CurrencyAPIView 


urlpatterns = [
    path('mainpage2/', CurrencyAPIView.as_view()),
]