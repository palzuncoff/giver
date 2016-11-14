from __future__ import unicode_literals

from partners.models import Partner

from django.db import models

class Gift(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    partner= models.ForeignKey(Partner, on_delete=models.CASCADE)
    end_offer_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    is_offer_avalabale = models.BooleanField()
    is_delivery = models.BooleanField(default=False)
    is_hot_offer = models.BooleanField(default=False)


class NameDiscriptionCategory(models.Model):
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)
    name_en=models.CharField(max_length=100)
    name_ro=models.CharField(max_length=100)
    name_ru=models.CharField(max_length=100)
    description_en = models.TextField(max_length=500)
    description_ro = models.TextField(max_length=500)
    description_ru = models.TextField(max_length=500)
    category_en = models.CharField(max_length=50)
    category_ro = models.CharField(max_length=50)
    category_ru = models.CharField(max_length=50)


    def __unicode__(self):
        return self.name_en

    def __unicode__(self):
        return self.name_ro

    def __unicode__(self):
        return self.name_ru

    def __unicode__(self):
        return self.category_en

    def __unicode__(self):
        return self.category_ro

    def __unicode__(self):
        return self.category_ru

    def __unicode__(self):
        return self.description_en

    def __unicode__(self):
        return self.description_ro

    def __unicode__(self):
        return self.description_ru



