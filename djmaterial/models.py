from __future__ import unicode_literals

from django.db import models


class Test(models.Model):
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    keep_logged = models.BooleanField()
