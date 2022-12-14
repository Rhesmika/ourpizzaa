# Generated by Django 3.2.16 on 2022-11-07 21:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='notes',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='booking',
            name='party_of',
            field=models.IntegerField(default=2, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
