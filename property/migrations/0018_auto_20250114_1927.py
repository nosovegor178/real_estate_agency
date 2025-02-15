# Generated by Django 2.2.24 on 2025-01-14 16:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20241224_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='complaint_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_pure_phone',
            new_name='pure_phone',
        ),
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_flats', to=settings.AUTH_USER_MODEL, verbose_name='Кому понравилось'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='flats_in_ownership',
            field=models.ManyToManyField(blank=True, related_name='owned_by', to='property.Flat', verbose_name='Квартиры во владении'),
        ),
    ]
