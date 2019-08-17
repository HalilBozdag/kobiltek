from django.db import models


class Branch(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField()
    name = models.CharField(blank=False, null=False, max_length=120)