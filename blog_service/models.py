# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=250, blank=True)
    slug = models.SlugField()
    content = models.CharField(max_length=250, blank=True)
    author = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title
