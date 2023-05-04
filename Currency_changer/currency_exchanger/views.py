from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests



class CurrencyAPIView(APIView):
    def get(self, request, *args, **kwargs):
        api_route = 'https://openexchangerates.org/api/latest.json?app_id=f39eeff3540a41fa919debe87b0071de'
        data = requests.get(api_route)
        return Response(data=data.json(), status=status.HTTP_200_OK)
        
    

    
