# Generated by Django 3.1.2 on 2020-10-04 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space_rangers', '0010_pilotfraction'),
    ]

    operations = [
        migrations.AddField(
            model_name='pilot',
            name='fractions',
            field=models.ManyToManyField(related_name='pilots', related_query_name='all_pilots', through='space_rangers.PilotFraction', to='space_rangers.Fraction'),
        ),
    ]