# Generated by Django 4.1.7 on 2023-02-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodApp', '0002_hospitals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitals',
            name='area',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='contact',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='hospital',
            field=models.CharField(default='', max_length=50),
        ),
    ]