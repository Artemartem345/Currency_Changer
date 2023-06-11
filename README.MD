# Currency_changer and converter




### For get course for currency:
http:127.0.0.1:/cur_page_course/?Currency='Your currency'

CURRENCY_CHOICES = (
    ('EUR', 'EUROPEAN CURRENCY'),
    ('USD', 'UNITED STATES DOLLAR'),
    ('RUB', 'RUSSIAN ROUBLE CURRENCY'),
    ('KZT', 'KAZAKHSTAN TENGE CURRENCY'),
    ('CAD', 'CANADIAN CURRENCY'),
    ('AUD', 'AUSTRALIAN DOLLAR CURRENCY'),
    ('AZN', 'AZERBAIJANIAN MANAT CURRENCY'),
    ('BGN', 'BULGARIAN LEV CURRENCY'),
    ('CZK', 'CZECH KORUNA CURRENCY'),
    ('DKK', 'DANISH CRONE CURRENCY'),
    ('EGP', 'EGYPTIAN POUND CURRENCY'),
    ('JPY', 'JAPANESE YEN CURRENCY'),
)

### to count the amount of currency for dollars

http:127.0.0.1:/cur_page_course/?Currency='Your currency'&amount='Your amount (Only int)'

### Shows currency courses from DataBase

http:127.0.0.1:/currencys/

### Get the JWT token
http:127.0.0.1:/token/


### verify the JWT token
http:127.0.0.1:/token/verify/


### Refresh the JWT token

http:127.0.0.1:/token/refresh/


### For registering the JWT token

http:127.0.0.1:/register/