# Generated by Django 4.1.7 on 2023-02-25 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BloodApp', '0021_alter_userdonorrequest_d_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acceptdonorlist',
            name='d_location',
        ),
        migrations.RemoveField(
            model_name='acceptdonorlist',
            name='d_visit',
        ),
    ]
