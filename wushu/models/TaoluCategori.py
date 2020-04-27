from django.db import models

from wushu.models.Athlete import Athlete


class TaoluCategori(models.Model):
    categoryName = models.CharField(max_length=255, null=True, blank=True)
    # compCategoryCompleted=models.BooleanField(null=True, blank=True)
    # compOrder=models.IntegerField(null=True, blank=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    isDuilian = models.BooleanField(null=True, blank=True)
    # kobilId=models.IntegerField(null=True, blank=True)
    operationDate = models.DateTimeField(auto_now_add=True)

    # playersOrdered=models.BooleanField(null=True, blank=True)
    # recordCompleted=models.BooleanField(null=True, blank=True)
    def __str__(self):
        return '%s' % (self.categoryName)

    class Meta:
        default_permissions = ()
