# Generated by Django 5.1.4 on 2025-01-21 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_alter_clasification_clasification_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_title', models.CharField(blank=True, max_length=250, null=True)),
                ('item_image', models.ImageField(blank=True, null=True, upload_to='item/')),
            ],
        ),
        migrations.DeleteModel(
            name='Clasification',
        ),
    ]
