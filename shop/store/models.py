from django.db import models


class Goods(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False, max_length=1000)
    name = models.CharField(max_length=100, null=False)
    categoryId = models.IntegerField(null=False, default='1')
    price = models.DecimalField(max_length=12, null=False, max_digits=10, decimal_places=2)


