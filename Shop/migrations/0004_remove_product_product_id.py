# Generated by Django 3.0.8 on 2020-08-24 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_product_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_id',
        ),
    ]
