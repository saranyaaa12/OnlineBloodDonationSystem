# Generated by Django 4.1.7 on 2023-03-06 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BloodApp', '0034_hospitals_links'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospitals',
            name='links',
        ),
    ]
