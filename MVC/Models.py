# Models.py
from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('用户名', max_length=20)

