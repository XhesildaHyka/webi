# Generated by Django 5.1.4 on 2025-01-15 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_remove_product_product_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(blank=True, max_length=250, null=True)),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='product/')),
            ],
        ),
    ]
