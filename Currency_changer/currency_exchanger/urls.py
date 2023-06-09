from django.contrib import admin
from django.urls import path
from .views import CurrencyAPIView, CourseAPIView, GetCourseAPIView, ShowCurrencyCourseFromDB, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('cur_page/', CurrencyAPIView.as_view(), name='currency_change'),
    path('cur_page_course/', CourseAPIView.as_view(), name='currency_course'),
    path('currencys/',  ShowCurrencyCourseFromDB.as_view(), name='all_curs_from_db'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'), 
    path('register/', RegisterView.as_view(), name='register'),
]