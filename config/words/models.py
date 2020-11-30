# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Words(models.Model):
    word_japanese = models.CharField(max_length=30)
    word_meaning = models.CharField(max_length=30)
