from django.contrib import admin
from .models import Currency, CurrencyRate
# Register your models here.

admin.site.register(Currency)
admin.site.register(CurrencyRate)
