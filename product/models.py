from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    code = models.CharField(max_length=3, primary_key=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    product_hsn = models.CharField(max_length=50, null=True, blank=True)
    code = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    discount = models.FloatField(default=0, help_text='discount in percentage')
    product_gst_percentage = models.FloatField(default=0)
    product_rate_with_gst = models.FloatField(default=0)

    # show_on_website = models.BooleanField(default=False)

    def __str__(self):
        return self.name
