
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CurrencyRate
from .services import *
from rest_framework.permissions import IsAuthenticated




# конвертация валюты
class CurrencyAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        currency = request.GET.get('currency')
        amount = request.GET.get('amount')
        update_currency_rate(currency)
        currency_calculate = calculate_currency(currency, amount=int(amount)) # first param is Code currency. The second param is count dollars
        return Response(data=currency_calculate, status=status.HTTP_200_OK)

class CourseAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        currency = request.GET.get('currency')
        currency_data = get_api_json()['rates'][currency]
        return Response(data={'currency_course':currency_data}, status=status.HTTP_200_OK)
   
class ShowCurrencyCourseFromDB(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        course = request.GET.get('course')
        currency = CurrencyRate.objects.filter(course__gt=course).values_list('currency__name', flat=True)
        return Response(data={'cur_data':set(currency)}, status=status.HTTP_200_OK)
        
