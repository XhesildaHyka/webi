# Generated by Django 5.1.5 on 2025-01-31 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0011_arrival_arrival_description_arrival_arrival_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arrival',
            name='arrival_description',
        ),
        migrations.RemoveField(
            model_name='arrival',
            name='arrival_price',
        ),
        migrations.AddField(
            model_name='product',
            name='product_arrival',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.arrival'),
        ),
    ]
