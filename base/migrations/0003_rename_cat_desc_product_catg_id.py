# Generated by Django 4.0.6 on 2022-09-06 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_catg_id_product_cat_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='cat_desc',
            new_name='catg_id',
        ),
    ]