from django.urls import path
from .views import CurrencyAPIView, CourseAPIView,  ShowCurrencyCourseFromDB


urlpatterns = [
    path('cur_page/', CurrencyAPIView.as_view(), name='currency_change'),
    path('cur_page_course/', CourseAPIView.as_view(), name='currency_course'),
    path('currencys/',  ShowCurrencyCourseFromDB.as_view(), name='all_curs_from_db')
]
