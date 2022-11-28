from django.db import models
from django.contrib.auth.models import User


class Station(models.Model):
    """
        Модель космической станции.
        name - имя станции
        state - состояние(running,broken)
        created_at - время создании записи
        destroyed_time - время когда станция сламалась, вышла за пределы положительных координат
        x - положение по x
        y - положение по y
        z - положение по z
    """
    class State(models.TextChoices):
        running = 'Running', 'Running'
        broken = 'Broken', 'Broken'

    name = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, choices=State.choices, default=State.running)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    destroyed_time = models.DateTimeField(null=True)
    x = models.IntegerField(default=100)
    y = models.IntegerField(default=100)
    z = models.IntegerField(default=100)

    def __str__(self):
        return self.name


class Instructions(models.Model):
    """
        Инструкция с помощью которой двигается космическая станция.
        user - пользователь который сделал инструкцию
        station - станция для которой была сделана инструкция
        axis - ось по которой нужно двигаться
        distance - дистанция на сколько двигаться
    """
    user: User = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    station: Station = models.ForeignKey(Station, null=True, on_delete=models.CASCADE)
    axis = models.CharField(max_length=30, null=True)
    distance = models.IntegerField()

    def __str__(self):
        return f'num:{self.pk},user:{self.user.username},station:{self.station.name}'
