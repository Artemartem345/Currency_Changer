from django.contrib import admin
from django.urls import path
from .views import CurrencyAPIView, CourseAPIView, GetCourseAPIView, ShowCurrencyCourseFromDB, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('cur_page/', CurrencyAPIView.as_view()),
    path('cur_page_course/', CourseAPIView.as_view()),
    path('cur_page_lt_10/', GetCourseAPIView.as_view()),
    path('currencys/',  ShowCurrencyCourseFromDB.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()), 
    path('register/', RegisterView.as_view()),
]