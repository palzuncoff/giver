from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models

class Partner(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    telephone = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

    def __unicode__(self):
        return self.description

    def __unicode__(self):
        return self.address




class AddressWhereTakeGift(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    delivery_notify = models.EmailField(max_length=100)
    adress = models.CharField(max_length=500)
    latitude = models.DecimalField(max_digits=12, decimal_places=10)
    longitude = models.DecimalField(max_digits=12, decimal_places=10)

    def __unicode__(self):
        return self.adress
