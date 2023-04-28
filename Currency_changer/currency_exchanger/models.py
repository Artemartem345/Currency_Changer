from django.db import models

# Create your models here.


CURRENCY_CHOICES = (
    ('EUR', 'EUROPEAN CURRENCY'),
    ('USD', 'UNITED STATES DOLLAR'),
    ('RUB', 'RUSSIAN ROUBLE'),
    ('YEN', 'JAPAN CURRENCY'),
    ('DIR', 'ARABIAN CURRENCY'),
    ('CAD', 'CANADIAN CURRENCY'),
    
)
class Currency:
    currency = models.CharField(max_length=150,choices=CURRENCY_CHOICES)
    
                                

class Course:
    currency = models.ForeignKey. 
    time_course = 
    course1 =     