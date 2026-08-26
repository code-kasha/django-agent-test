from django.db import models


class Item(models.Model):
    """
    Represents an item in the inventory.
    """

    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=64, unique=True)
    quantity = models.IntegerField()
