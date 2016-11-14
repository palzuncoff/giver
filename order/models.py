from __future__ import unicode_literals

from django.db import models

from gift.models import Gift

from members.models import Member



class Order(models.Model):
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    #friend = models.ForeignKey()
    is_surprise = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    is_taken = models.BooleanField(default=False)
    additional_delivery_address = models.CharField(max_length=100, blank=True)
    additional_delivery_phone_number = models.CharField(max_length=20, blank=True)
    delivery_time = models.DateTimeField(blank=True)


    def __unicode__(self):
        return self.delivery_address


class Statistic(models.Model):
    pass
