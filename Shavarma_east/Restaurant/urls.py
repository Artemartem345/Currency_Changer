from django.urls import path

from .views import func, func1, func2
from . import views


class SiteMenu:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
        
        

page = SiteMenu(name='shavarma_mexico', price='280', description='Meat, vegetables and pita')

page1 = SiteMenu(name='shavarma_with_cheese_pita', price='250', description='cheese pita and other')
















urlpatterns = [
    path('', views.func, name='func'),
]