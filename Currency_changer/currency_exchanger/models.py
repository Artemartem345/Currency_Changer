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
    ('DKK', 'DANISH CRONE'),
    ('EGP', 'EGYPTIAN POUND CURRENCY'),
    ('JPY', 'JAPANESE YEN CURRENCY')
)
class Currency(models.Model):
    currency = models.CharField(max_length=150,choices=CURRENCY_CHOICES)
    
                                

class Course(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    course = models.FloatField()    