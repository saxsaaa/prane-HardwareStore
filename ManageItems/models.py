from django.db import models

class hwItems(models.Model):
    hwItem = models. SmallIntegerField(primary_key=True)
    hwName = models.CharField(max_length=50)
    hwDescription = models.TextField(max_length=200)
    hwQty = models.SmallIntegerField
