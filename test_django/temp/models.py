from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Scripts(models.Model):#  Основной список всех платы (устройств)
    vin = models.CharField(verbose_name='vin', db_index=True, unique=True, max_length=64)

    weatherstation = models.CharField(verbose_name='weatherstation', max_length=64)


class Temp1(models.Model):# Первая плата (устройств)
    Temp1 = models.ForeignKey(Scripts, on_delete=models.CASCADE, related_name='Temp1', null=True, blank=True) # Вложения в основной список

    #########################
    Temperature = models.CharField(verbose_name='Temperature', max_length=64,default='100')# Тепература с датчика
    Humidity = models.CharField(verbose_name='Humidity', max_length=64,default='100')# Влажность с датчика
    TemperatureLOW = models.CharField(verbose_name='TemperatureLOW', max_length=64, default='1')# Нижний предел температуры
    HumidityLOW = models.CharField(verbose_name='HumidityLOW', max_length=64, default='1')# Нижний предел  влажности
    TemperatureHigh = models.CharField(verbose_name='TemperatureHigh', max_length=64, default='100')# Верхний предел температуры
    HumidityHigh = models.CharField(verbose_name='HumidityHigh', max_length=64, default='100')#Верхний предел влажности
    #########################


class Temp2(models.Model):
    Temp2 = models.ForeignKey(Scripts, on_delete=models.CASCADE, related_name='Temp2', null=True, blank=True)

    #########################
    Temperature = models.CharField(verbose_name='Temperature', max_length=64, default='100')
    Humidity = models.CharField(verbose_name='Humidity', max_length=64, default='100')
    TemperatureLOW = models.CharField(verbose_name='TemperatureLOW', max_length=64, default='1')
    HumidityLOW = models.CharField(verbose_name='HumidityLOW', max_length=64, default='1')
    TemperatureHigh = models.CharField(verbose_name='TemperatureHigh', max_length=64, default='100')
    HumidityHigh = models.CharField(verbose_name='HumidityHigh', max_length=64, default='100')


class Temp3(models.Model):
    Temp3 = models.ForeignKey(Scripts, on_delete=models.CASCADE, related_name='Temp3', null=True, blank=True)

    #########################
    Temperature = models.CharField(verbose_name='Temperature', max_length=64, default='100')
    Humidity = models.CharField(verbose_name='Humidity', max_length=64, default='100')
    TemperatureLOW = models.CharField(verbose_name='TemperatureLOW', max_length=64, default='1')
    HumidityLOW = models.CharField(verbose_name='HumidityLOW', max_length=64, default='1')
    TemperatureHigh = models.CharField(verbose_name='TemperatureHigh', max_length=64, default='100')
    HumidityHigh = models.CharField(verbose_name='HumidityHigh', max_length=64, default='100')
