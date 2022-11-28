import datetime

from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Instructions, Station


@receiver(post_save, sender=Instructions)
def instruction_created_handler(sender, instance, created, **kwargs) -> None:
    if created:
        station = Station.objects.get(pk=instance.station.pk)

        if instance.axis == 'x':
            station.x += instance.distance

        if instance.axis == 'y':
            station.y += instance.distance

        if instance.axis == 'z':
            station.z += instance.distance

        check_if_station_working(station)

        station.save()


def check_if_station_working(station: Station):
    if station.z < 0 or station.x < 0 or station.y < 0:
        station.state = 'broken'
        station.destroyed_time = timezone.now()
