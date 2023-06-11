from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import SignUpSerializer
# Create your views here.

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