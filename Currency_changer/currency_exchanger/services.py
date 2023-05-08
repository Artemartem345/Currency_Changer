
from .models import CurrencyRate, Currency

def calculate(currency:str, amount:int):
    var = Currency.objects.get(currency=currency)
    return CurrencyRate.objects.filter(var) 
    
