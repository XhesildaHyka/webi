# Generated by Django 5.1.4 on 2025-01-20 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_product_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_sms', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_new',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='product_trade',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to='category/'),
        ),
    ]
