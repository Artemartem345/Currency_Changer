from django.contrib import admin
from django.urls import path
from Store import views


urlpatterns = [
    path('products', views.show_info),
    path('add_food', views.add_food, name='add_food'),
    

    
    
]