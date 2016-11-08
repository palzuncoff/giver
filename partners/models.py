from __future__ import unicode_literals

from django.db import models

class Partner(models.Model):
    name= models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    telephone = models.CharField(max_length=20)


class AddressWhereTakeGift(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    adress = models.CharField(max_length=500)
    latitude = models.DecimalField(max_digits=12, decimal_places=10)
    longitude = models.DecimalField(max_digits=12, decimal_places=10)