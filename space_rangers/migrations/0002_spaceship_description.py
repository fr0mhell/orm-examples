# Generated by Django 3.1.2 on 2020-10-04 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space_rangers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spaceship',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]