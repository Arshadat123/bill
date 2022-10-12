from django.db import models

from product.models import Product


class Item(models.Model):
    item = models.ForeignKey(Product, related_name="quantity", on_delete=models.RESTRICT)
    bill = models.ForeignKey("Bill", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)


# Create your models here.
class Bill(models.Model):
    # bill_no = models.AutoField()
    customer_name = models.CharField(max_length=100, null=True, blank=True)

    date = models.DateTimeField(auto_created=True)
    product = models.ManyToManyField(Product, through=Item, related_name="bill")
