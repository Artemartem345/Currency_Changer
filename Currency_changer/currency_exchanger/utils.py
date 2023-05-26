import requests
from rest_framework.response import Response

class DataMixin:
    def get(self, request):
        course_data = request.GET.get('currency')
        api_route = 'https://openexchangerates.org/api/latest.json?app_id=f39eeff3540a41fa919debe87b0071de'
        data = requests.get(api_route)
        _data = data.json()
        currency_data = _data['rates'][course_data]
        return Response(data={'currency_course':currency_data}, status=status.HTTP_200_OK)
    