from __future__ import unicode_literals

from django.db.models import ImageField

from giver.settings import MEDIA_ROOT

from partners.models import Partner

from django.db import models



def get_image_path(instance, filename):
    return "category_logo/picture.jpg"


class Category(models.Model):
    logo = models.ImageField(upload_to=get_image_path, null=True)
    category_en = models.CharField(max_length=50)
    category_ro = models.CharField(max_length=50)
    category_ru = models.CharField(max_length=50)

    def __unicode__(self):
        return self.category_en

    def __unicode__(self):
        return self.category_ro

    def __unicode__(self):
        return self.category_ru

    def image_img(self):
        if self.gift_picture:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.logo.url)
        else:
            return '(no picture)'
    image_img.short_description = 'Picture'
    image_img.allow_tags = True


class Gift(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
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



    def __unicode__(self):
        return self.name_en

    def __unicode__(self):
        return self.name_ro

    def __unicode__(self):
        return self.name_ru


    def __unicode__(self):
        return self.description_en

    def __unicode__(self):
        return self.description_ro

    def __unicode__(self):
        return self.description_ru



