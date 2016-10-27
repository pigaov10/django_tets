# -*- coding: utf-8

from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
#timezone.now()

class Category(models.Model):
    name = models.CharField('Categoria',
                            max_length=25)

    def __str__(self):
        return self.name
