import celery 
from .models import CurrencyRate, Currency
from datetime import datetime




def calculate(currency:str, amount:int) -> CurrencyRate:
    
    return CurrencyRate.objects.filter(course__gt=10)
 

def calculate_currency(currency:str, amount:int):
    currency_rate =  CurrencyRate.objects.filter(currency__name=currency)[0]
    
    currency_course = currency_rate.course * amount
    result = {
        'result':f'You changed the {amount} USD on the: {currency_course} {currency}, for time:  {currency_rate.date_time}'
        
        }
    return  result

    




'''



In SubCategory model you have a field named country which refers to ProductCategory. You can't filter with productcategory_id because there is no such column/field in current model.

 class SubCategory(models.Model):
     country = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
     name = models.CharField(max_length=30)

     def __str__(self):
        return self.name 

So try to fix your queries like below in forms.py and views.py :

SubCategory.objects.filter(country_id=productcategory_id).order_by('name')



'''