from __future__ import unicode_literals

from django.db.models import ImageField

from giver.settings import MEDIA_ROOT

from django.contrib.auth.models import User

from django.db import models

def get_image_path(instance, filename):
    return "partner_logo/picture.jpg"

class Partner(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to=get_image_path, null=True)
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    telephone = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

    def __unicode__(self):
        return self.description

    def __unicode__(self):
        return self.address

    def image_img(self):
        if self.gift_picture:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.gift_picture.url)
        else:
            return '(no picture)'
    image_img.short_description = 'Picture'
    image_img.allow_tags = True




class AddressWhereTakeGift(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    delivery_notify = models.EmailField(max_length=100)
    adress = models.CharField(max_length=500)
    latitude = models.DecimalField(max_digits=12, decimal_places=10)
    longitude = models.DecimalField(max_digits=12, decimal_places=10)

    def __unicode__(self):
        return self.adress
