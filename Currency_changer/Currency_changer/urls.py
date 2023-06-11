from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name=...),
    path('', include('currency_exchanger.urls'), name=...),
    path('', include('Users.urls'))
]

