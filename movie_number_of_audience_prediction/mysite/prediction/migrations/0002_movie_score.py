# Generated by Django 3.2.6 on 2021-09-01 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]
