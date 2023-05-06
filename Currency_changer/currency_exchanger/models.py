from django.db import models

# Create your models here.


CURRENCY_CHOICES = (
    ('EUR', 'EUROPEAN CURRENCY'),
    ('USD', 'UNITED STATES DOLLAR'),
    ('RUB', 'RUSSIAN ROUBLE CURRENCY'),
    ('YEN', 'JAPAN CURRENCY'),
    ('DIR', 'ARABIAN CURRENCY'),
    ('CAD', 'CANADIAN CURRENCY'),
    ('AUD', 'AUSTRALIAN DOLLAR CURRENCY'),
    ('AZN', 'AZERBAIJANIAN MANAT CURRENCY'),
    ('BGN', 'BULGARIAN LEV CURRENCY'),
    ('CZK', 'CZECH KORUNA CURRENCY'),
    ('DKK', 'DANISH CRONE CURRENCY'),
    ('EGP', 'EGYPTIAN POUND CURRENCY'),
    ('JPY', 'JAPANESE YEN CURRENCY'),
)
class Currency(models.Model):
    name = models.CharField(max_length=150,choices=CURRENCY_CHOICES)
    def __str__(self):
        return self.name 
  
                                

class CurrencyRate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    course = models.DecimalField(max_digits=10, decimal_places=4)
    
        