# Generated by Django 4.1.9 on 2023-06-21 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboards', '0006_delete_laptops'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptops',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('link', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS')),
                ('brand', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS')),
                ('warranty', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS')),
                ('processor', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS')),
                ('ram', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS')),
                ('harddrive', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='hardDrive')),
                ('grapcard', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='grapCard')),
                ('capgrapcard', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='capGrapCard')),
                ('opsystem', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='opSystem')),
                ('screensize', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='screenSize')),
                ('price', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS')),
                ('ram_gb_field', models.IntegerField(blank=True, db_column='ram (GB)')),
                ('warranty_meses_field', models.FloatField(blank=True, db_column='warranty (meses)')),
                ('screensize_pulgadas_field', models.FloatField(blank=True, db_column='screenSize (Pulgadas)')),
                ('price_cops_field', models.FloatField(blank=True, db_column='price (COPs)')),
                ('marketplace', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='marketPlace')),
            ],
            options={
                'verbose_name': 'Laptop',
                'verbose_name_plural': 'Laptops',
                'db_table': 'Laptops',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dashboards', to=settings.AUTH_USER_MODEL),
        ),
    ]
