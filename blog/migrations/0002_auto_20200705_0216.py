# Generated by Django 3.0.8 on 2020-07-05 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_path',
            field=models.SlugField(max_length=200),
        ),
    ]
