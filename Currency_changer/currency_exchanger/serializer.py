from rest_framework import serializers
from .models import CurrencyRate, Currency, CustomUser



class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('currency', 'course')
        
class CurrencyRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = '__all__'

class SignUpSerializer(serializers.ModelSerializer):    
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser        
        fields = ['email', 'firstname', 'lastname', 'password', 'password2']
        extra_kwargs = {            
        'password': {'write_only': True}
        }
    def save(self, **kwargs):        
        user = CustomUser(email=self.validated_data['email'],
        firstname=self.validated_data['firstname'],                          
        lastname=self.validated_data['lastname'])
        password, password2 = self.validated_data['password'], self.validated_data['password2']        
        if password != password2:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})        
        user.set_password(password)
        user.save()        
        return user