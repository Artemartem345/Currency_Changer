from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import RegisterView

urlpatterns= [
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'), 
    path('register/', RegisterView.as_view(), name='register'),
]