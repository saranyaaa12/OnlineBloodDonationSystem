# Generated by Django 4.1.7 on 2023-02-25 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BloodApp', '0022_remove_acceptdonorlist_d_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rejectdonorlist',
            name='d_location',
        ),
        migrations.RemoveField(
            model_name='rejectdonorlist',
            name='d_visit',
        ),
    ]
