# Generated by Django 3.0.8 on 2020-08-01 06:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200801_0319'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='difficulty',
            field=models.PositiveIntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='game',
            name='difficultyLeft',
            field=models.PositiveIntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='game',
            name='trailer1',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='game',
            name='trailer2',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='game',
            name='trailer3',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
