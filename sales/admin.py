from django.contrib import admin

from sales import models


class Quantity(admin.TabularInline):
    model = models.Item


@admin.register(models.Bill)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'date', ]

    inlines = [Quantity]

    search_fields = ['id', 'customer_name']
