from .cfg import open_exchanger_api_url
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
    data = requests.get(open_exchanger_api_url)
    _data = data.json()
    currency_data = _data['rates']['KZT']
    return currency_data

def get_all_currency():
    data = requests.get(open_exchanger_api_url)
    data_json = data.json()
    all_currency_data = data_json['rates']
    return all_currency_data

def get_api_json():
    data = requests.get(open_exchanger_api_url)
    return data.json()
    
def create_currency_rate_obj(cur, currency_data):
    currency_rate = CurrencyRate.objects.create(currency=cur, course=currency_data)
    currency_rate.save()


def update_currency_rate(query_data):
    currency_data = get_api_json()['rates'][query_data]
    cur = Currency.objects.get_or_create(name=query_data)  
    print(cur)
    create_currency_rate_obj(cur[0], currency_data)
    

