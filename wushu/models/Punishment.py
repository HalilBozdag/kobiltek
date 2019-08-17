from django.db import models

from wushu.models import CategoryItem


class Punishment(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField()
    startDate = models.DateTimeField()
    expireDate = models.DateTimeField()
    durationDay = models.IntegerField()
    definition = models.ForeignKey(CategoryItem, on_delete=models.CASCADE())
    description = models.CharField(blank=True, null=True, max_length=1000)