# Generated by Django 4.2.11 on 2025-03-05 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='current date'),
        ),
    ]
