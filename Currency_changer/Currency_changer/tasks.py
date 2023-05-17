from __future__ import absolute_import
from .celery import app
from currency_exchanger.services import get_currency, get_all_currency
from datetime import timedelta
from currency_exchanger.models import Currency, CurrencyRate
# @app.task(name='update_currency')
# def update_currency():
#     result = get_currency()
#     cur = Currency.objects.get(name='KZT')
#     update_database = CurrencyRate.objects.create(currency=cur, course=result)
#     update_database.save()


@app.task(name='update_all_currency')
def update_all_currency():
    res = get_all_currency()
    cur = Currency.objects.all() 
    update_database = CurrencyRate.objects.create(currency=cur, course=res)
    update_database.save() 
    
    for c in cur:
        c.get('name') 
        print(cur)

app.conf.beat_schedule = {
    'run_me_every_15_sec':{
        'task':'update_all_currency',
        'schedule':timedelta(seconds=15),
        
        
    }
    
}


    
    
    

