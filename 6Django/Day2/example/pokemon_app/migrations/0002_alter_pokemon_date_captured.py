# Generated by Django 4.2 on 2023-07-18 04:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='date_captured',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]