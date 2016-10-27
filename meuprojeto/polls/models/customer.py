# -*- coding: utf-8

from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from category import Category
#timezone.now()

@python_2_unicode_compatible
class Customer(models.Model):
    first_name = models.CharField('nome', max_length=45)
    last_name = models.CharField('sobrenome', max_length=45)
    status = models.IntegerField('status')
    # created = models.DateTimeField('data_criacao', default=datetime.now())
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.first_name

    # class Meta:
    #     app_label = 'customer'
