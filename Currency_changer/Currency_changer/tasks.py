from __future__ import absolute_import
from .celery import app
from currency_exchanger.services import get_currency
from datetime import timedelta
from currency_exchanger.models import Currency, CurrencyRate
@app.task(name='update_currency')
def update_currency():
    result = get_currency()
    cur = Currency.objects.get(name='KZT')
    update_database = CurrencyRate.objects.create(currency=cur, course=result)
    update_database.save()
        
    

app.conf.beat_schedule = {
    'run_me_every_15_sec':{
        'task':'update_currency',
        'schedule':timedelta(seconds=15),
        
        
    }
    
}


    
    
    

