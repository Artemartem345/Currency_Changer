from django.shortcuts import render
from django.http import HttpResponse
import serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




class CurrencyAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK) 

def main_page(request):
    data = request
    
