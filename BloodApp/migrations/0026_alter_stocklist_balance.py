# Generated by Django 4.1.7 on 2023-03-03 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodApp', '0025_stocklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocklist',
            name='balance',
            field=models.IntegerField(),
        ),
    ]
