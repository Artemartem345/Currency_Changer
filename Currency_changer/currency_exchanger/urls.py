from django.contrib import admin
from django.urls import path
from .views import CurrencyAPIView, CourseAPIView, GetCourseAPIView


urlpatterns = [
    path('cur_page/', CurrencyAPIView.as_view()),
    path('cur_page_course/', CourseAPIView.as_view()),
    path('cur_page_lt_10/', GetCourseAPIView.as_view()),
]