
from .models import CurrencyRate, Currency
from datetime import datetime
import requests



def calculate(currency:str, amount:int) -> CurrencyRate:
    
    return CurrencyRate.objects.filter(course__gt=10)
 

def calculate_currency(currency:str, amount:int):
    currency_rate =  CurrencyRate.objects.filter(currency__name=currency)[0]
    
    currency_course = currency_rate.course * amount
    result = {
        'result':f'You changed the {amount} USD on the: {currency_course} {currency}, for time:  {currency_rate.date_time}'
        
        }
    return  result

def get_currency():
    api_route = 'https://openexchangerates.org/api/latest.json?app_id=f39eeff3540a41fa919debe87b0071de'
    data = requests.get(api_route)
    _data = data.json()
    currency_data = _data['rates']['KZT']
    return currency_data

def get_all_currency():
    api_route = 'https://openexchangerates.org/api/latest.json?app_id=f39eeff3540a41fa919debe87b0071de'
    data = requests.get(api_route)
    data_json = data.json()
    all_currency_data = data_json['rates']


    




