from django.contrib import admin
from django.urls import path
from .views import main_page


urlpatterns = [
    path('mainpage2/', main_page),
]