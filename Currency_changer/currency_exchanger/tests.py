from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

class CurrencyAPITests(APITestCase):
    client = APIClient()
    
    
    def authenticate(self):
        
        user_reg_data = {
            'email': 'artemartem@gmail.com',
            'firstname': 'artem',
            'lastname': 'Artem',
            'password': 'Artem123',
            'password2': 'Artem123',
            }
        
        response = self.client.post(reverse('currency_change', user_reg_data))
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {response.data["access"]}')
         
    def test_http_status(self):
        data = {
            
        }
                
'''

1. написать тест для куренси апи вью, чтобы была проверка на ввод количества(amount)

'''        

        
        

 

