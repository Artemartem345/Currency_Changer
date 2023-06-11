from __future__ import absolute_import
from .celery import app
from currency_exchanger.services import get_currency, get_all_currency
from datetime import timedelta
from currency_exchanger.models import Currency, CurrencyRate
@app.task(name='update_currency')
def update_currency():
    result = get_currency()
    cur = Currency.objects.get(name='KZT')
    update_database = CurrencyRate.objects.create(currency=cur, course=result)
    update_database.save()


@app.task(name='update_all_currency')
def update_all_currency():
    cur = Currency.objects.all() 
    all_cur = get_all_currency()
    for c in cur:
       cur_course = all_cur[c.name]
       CurrencyRate.objects.create(currency=c, course=cur_course)
       
# @app.task(name='get_exact_currency')
# def get_exact_currency():
#     res = get_cur_less_than_10_dolar()
#     cur = Currency.objects.all(name__qt=10)
    


       
    
        
                
        
        
        
    
   
        
        
        

        
        
         
        

app.conf.beat_schedule = {
    'run_me_every_15_sec':{
        'task':'update_all_currency',
        'schedule':timedelta(seconds=15),
        
        
    }
    
}


    
    
    

