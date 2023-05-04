from rest_framework import serializers
from models import Currency, Course


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('currency', 'course')


