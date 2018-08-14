# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import django_tables2 as tables

class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='full name')