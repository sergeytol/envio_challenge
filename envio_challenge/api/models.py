from django.db import models
from timescale.db.models.fields import TimescaleDateTimeField
from timescale.db.models.managers import TimescaleManager


class Reading(models.Model):
    time = TimescaleDateTimeField(interval="1 day")
    reading = models.FloatField()
    device_id = models.UUIDField()
    customer_id = models.UUIDField()

    objects = models.Manager()
    timescale = TimescaleManager()

    class Meta:
        indexes = [
            models.Index(fields=['device_id']),
            models.Index(fields=['customer_id']),
        ]
