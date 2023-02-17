# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 02:17:38 2023

@author: BEAST OF DARKNESS
"""
from django.db import models
from django.contrib.postgres.fields import ArrayField

class NETWORK(models.Model):
    company = ArrayField(
        ArrayField(
            models.CharField(max_length=32, blank=True),
            size=8,
        ),
        size=8,
    )
    gbfs_href = models.CharField(max_length = 256)
    href = models.CharField(max_length = 128)
    id = models.CharField(max_length = 32, primary_key = True)
    name = models.CharField(max_length = 32)
    location_city = models.CharField(max_length = 128)
    location_country = models.CharField(max_length = 128)
    location_latitude = models.FloatField()
    location_longitude = models.FloatField()
    
    
class STATIONS(models.Model):
    empty_slots = models.IntegerField()
    free_bikes = models.IntegerField()
    id = models.CharField(max_length = 64, primary_key = True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=128)
    timestamp = models.DateTimeField()
    extra_altitude = models.FloatField()
    extra_ebikes = models.IntegerField()
    extra_has_ebikes = models.BooleanField()
    extra_has_ebikes = models.BigIntegerField()
    extra_normal_bikes = models.IntegerField()
    extra_payment = ArrayField(
            ArrayField(
                models.CharField(max_length=32, blank=True),
                size=8,
            ),
            size=8,
        )
    extra_payment_terminal = models.BooleanField()
    extra_post_code = models.BigIntegerField()
    extra_renting = models.BooleanField()
    extra_returning = models.IntegerField()
    extra_slots = models.IntegerField()
    extra_uid = models.IntegerField()
    