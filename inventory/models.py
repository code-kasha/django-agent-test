from django.db import models


class Item(models.Model):
    """
    Represents an inventory item with name, SKU, and quantity.
    """

    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=64, unique=True)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
