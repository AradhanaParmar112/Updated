# Generated by Django 4.1.1 on 2022-09-21 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burt', '0002_helpermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpermodel',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
