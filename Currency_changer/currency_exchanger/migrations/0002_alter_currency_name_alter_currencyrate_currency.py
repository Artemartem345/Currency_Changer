# Generated by Django 4.1.7 on 2023-05-06 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currency_exchanger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(choices=[('EUR', 'EUROPEAN CURRENCY'), ('USD', 'UNITED STATES DOLLAR'), ('RUB', 'RUSSIAN ROUBLE CURRENCY'), ('DIR', 'ARABIAN CURRENCY'), ('CAD', 'CANADIAN CURRENCY'), ('AUD', 'AUSTRALIAN DOLLAR CURRENCY'), ('AZN', 'AZERBAIJANIAN MANAT CURRENCY'), ('BGN', 'BULGARIAN LEV CURRENCY'), ('CZK', 'CZECH KORUNA CURRENCY'), ('DKK', 'DANISH CRONE CURRENCY'), ('EGP', 'EGYPTIAN POUND CURRENCY'), ('JPY', 'JAPANESE YEN CURRENCY')], max_length=150),
        ),
        migrations.AlterField(
            model_name='currencyrate',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currency_exchanger.currency'),
        ),
    ]