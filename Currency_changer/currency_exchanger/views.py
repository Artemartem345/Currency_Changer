from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import CurrencyRate, Currency
from .serializer import CurrencyRateSerializer, CurrencySerializer
from .services import calculate

class CurrencyAPIView(APIView):
    def get(self, request, *args, **kwargs):
        query_data = request.GET.get('currency')
        if query_data is None:
            return Response(status=404)
        print(query_data)
        api_route = 'https://openexchangerates.org/api/latest.json?app_id=f39eeff3540a41fa919debe87b0071de'
        data = requests.get(api_route)
        _data = data.json()
        # Dollar data
        currency_data = _data['rates'][query_data]
        # CurrencyRate.objects.create()
        # Currency django admin
        cur = Currency.objects.get(name=query_data)  
        currency_rate = CurrencyRate.objects.create(currency=cur, course=currency_data)
        currency_rate.save()
        serializer = CurrencyRateSerializer(currency_rate)
        # if serializer.is_valid():
        #     serializer.save()
        print(calculate('USD', '20'))
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
        
    

    
