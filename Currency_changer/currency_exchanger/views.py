from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import CurrencyRate, Currency



class CurrencyAPIView(APIView):
    def get(self, request, *args, **kwargs):
        api_route = 'https://openexchangerates.org/api/latest.json?app_id=f39eeff3540a41fa919debe87b0071de'
        data = requests.get(api_route)
        new_data = data.json()
        data_dollar = new_data['rates']['USD']
        # CurrencyRate.objects.create()
        currency = Currency.objects.get(name='USD')
        currency_rate = CurrencyRate.objects.create(currency=currency, rate=data_dollar)
        currency_rate.save()
        print(currency)
        return Response(data=currency_rate, status=status.HTTP_200_OK)
    
    def get(self, request, *args, **kwargs):
        api_route = 'https://openexchangerates.org/api/latest.json?app_id=f39eeff3540a41fa919debe87b0071de'
        data = requests.get(api_route)
        new_data = data.json()
        data_RUB = new_data['rates']['RUB']
        currency = Currency.objects.get(name='RUB')
        currency_rate = CurrencyRate.objects.create(currency=currency, rate=data_RUB)
        currency_rate.save()
        print(currency)
        return Response(data=currency_rate, status=status.HTTP_200_OK) 
        
    
    
        
    

    
