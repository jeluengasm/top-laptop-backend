from django.contrib import admin
from dashboards import models


@admin.register(models.Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
    )
    list_filter = ('is_published',)


@admin.register(models.Laptops)
class LaptopsAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'link',
        'warranty',
        'processor',
        'ram',
        'harddrive',
        'grapcard',
        'capgrapcard',
        'opsystem',
        'screensize',
        'price_cops_field',
        'ram_gb_field',
        'warranty_meses_field',
        'screensize_pulgadas_field',
        'marketplace'
    )
    list_filter = ('brand', 'opsystem', 'marketplace')
