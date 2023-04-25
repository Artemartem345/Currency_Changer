from django.shortcuts import render
from .models import Rubbish, Food
from django.http import HttpResponse
# Create your views here.


def show_info(request):
    food = Food.objects.all()
    
    return render(request, 'index.html', context={'food': food})


def add_food(request):
    if request.method == 'POST':
        print(request.POST)
        
        food = Food.objects.create(title=request.POST.get('title'), price=int(request.POST.get('price')) , href=request.POST.get('href') + '.com')
        
        
    return render(request, 'add_food.html')


