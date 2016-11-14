from __future__ import unicode_literals

from django.db import models

from gift.models import Gift

from partners.models import Partner

from django.db.models import ImageField


from giver.settings import MEDIA_ROOT


def get_image_path(instance, filename):
    return "img/picture.jpg"


class GiftGalery(models.Model):
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)
    gift_picture = models.ImageField(upload_to=get_image_path, null=True)


    def image_img(self):
        if self.gift_picture:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.gift_picture.url)
        else:
            return '(no picture)'
    image_img.short_description = 'Picture'
    image_img.allow_tags = True


class PartnerGalery(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    partner_picture = models.ImageField(upload_to=get_image_path, null=True)


    def image_img(self):
        if self.partner_picture:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.partner_picture.url)
        else:
            return '(no picture)'
    image_img.short_description = 'Picture'
    image_img.allow_tags = True


