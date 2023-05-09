
from .models import CurrencyRate, Currency

def calculate(currency:str, amount:int) -> CurrencyRate:
    var = Currency.objects.get(currency=currency)
    return CurrencyRate.objects.filter(var).order_by(amount) 
    
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