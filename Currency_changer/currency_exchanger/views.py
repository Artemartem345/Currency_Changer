from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import CurrencyRate, Currency
from .serializer import CurrencyRateSerializer, CurrencySerializer, SignUpSerializer
from .services import calculate_currency, get_all_currency
from rest_framework.permissions import IsAuthenticated
class CurrencyAPIView(APIView):
    def get(self, request):
        query_data = request.GET.get('currency')
        amount_data = request.GET.get('amount')
        if query_data is None:
            return Response(status=404)
        print(query_data)
        api_route = 'https://openexchangerates.org/api/latest.json?app_id=f39eeff3540a41fa919debe87b0071de'
        data = requests.get(api_route)
        _data = data.json()
        currency_data = _data['rates'][query_data]
        cur = Currency.objects.get(name=query_data)  
        currency_rate = CurrencyRate.objects.create(currency=cur, course=currency_data)
        currency_rate.save()
        serializer = CurrencyRateSerializer(currency_rate)
        
        
        currency_calculate = calculate_currency(query_data, amount=int(amount_data)) # first param is Code currency. The second param is count dollars
        return Response(data=currency_calculate, status=status.HTTP_200_OK)
    
class CourseAPIView(APIView):
    def get(self, request):
        course_data = request.GET.get('currency')
        api_route = 'https://openexchangerates.org/api/latest.json?app_id=f39eeff3540a41fa919debe87b0071de'
        data = requests.get(api_route)
        _data = data.json()
        currency_data = _data['rates'][course_data]
        return Response(data={'currency_course':currency_data}, status=status.HTTP_200_OK)
    
class GetCourseAPIView(APIView):
    def get(self, request):
        api_route = 'https://openexchangerates.org/api/latest.json?app_id=f39eeff3540a41fa919debe87b0071de'
        data = requests.get(api_route)
        data_json = data.json()
        currency_data = data_json['rates']
        cur_lt_10_dollar = {}
        for key, value in currency_data.items():
            if value <= 1.0:
                cur_lt_10_dollar[key] = value
        return Response(data={'cur': cur_lt_10_dollar}, status=status.HTTP_200_OK)
        
    
class ShowCurrencyCourseFromDB(APIView):
    def get(self, request):
        cur_data_course = request.GET.get('course')
        cur = CurrencyRate.objects.filter(course__gt=cur_data_course).values_list('currency__name', flat=True)
        return Response(data={'cur_data':set(cur)}, status=status.HTTP_200_OK)
        
        
        #   cur = Currency.objects.get(name=query_data)  
        # currency_rate = CurrencyRate.objects.create(currency=cur, course=currency_data)
        # currency_rate.save()
        # serializer = CurrencyRateSerializer(currency_rate)
        
class RegisterView(APIView):    
    permission_classes = []
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
    def post(self, request):        
        serializer = SignUpSerializer(data=request.data)        
        if serializer.is_valid():
            serializer.save()            
            return Response(data={'email': serializer.data['email']}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
            
    

    
