# Generated by Django 4.0.6 on 2022-10-29 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0005_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('userCity', models.TextField(blank=True, max_length=20)),
                ('userStreetNumber', models.TextField(blank=True, max_length=30)),
                ('userMobile', models.TextField(blank=True, max_length=20)),
                ('userCreditCardNumber', models.CharField(blank=True, max_length=16)),
                ('userCreditCard3Digit', models.CharField(blank=True, max_length=3)),
                ('userCreditCardExpiryDate', models.CharField(blank=True, max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
