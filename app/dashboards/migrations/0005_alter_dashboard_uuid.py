# Generated by Django 4.1.9 on 2023-06-21 12:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0004_alter_dashboard_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
