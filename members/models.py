from __future__ import unicode_literals

from django.conf import settings

from django.db import models

from django.db.models.signals import post_save

from django.dispatch import receiver

from django_facebook.models import FacebookModel, get_user_model

from django_facebook.utils import get_profile_model

import logging

from django.contrib.auth.models import User



class Member():
    pass
