from django.db import models
from django.utils.translation import gettext_lazy as _


class Laptops(models.Model):
    link = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True)
    brand = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True)
    warranty = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True)
    processor = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True)
    ram = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True)
    harddrive = models.TextField(db_column='hardDrive', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True)
    grapcard = models.TextField(db_column='grapCard', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True)
    capgrapcard = models.TextField(db_column='capGrapCard', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True)
    opsystem = models.TextField(db_column='opSystem', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True)
    screensize = models.TextField(db_column='screenSize', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True)
    price_cops_field = models.TextField(db_column='price (COPs)', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True)
    ram_gb_field = models.TextField(db_column='ram (GB)', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True)
    warranty_meses_field = models.TextField(db_column='warranty (meses)', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True)
    screensize_pulgadas_field = models.TextField(db_column='screenSize (Pulgadas)', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True)
    marketplace = models.TextField(db_column='marketPlace', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True)

    class Meta:
        managed = False
        db_table = 'Laptops'
        verbose_name = _('Laptop')
        verbose_name_plural = _('Laptops')


class Dashboard(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    embed_url = models.URLField(max_length=255, blank=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Dashboard')
        verbose_name_plural = _('Dashboards')

    def __str__(self):
        return self.title
