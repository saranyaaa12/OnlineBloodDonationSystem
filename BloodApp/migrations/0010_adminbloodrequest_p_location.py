# Generated by Django 4.1.7 on 2023-02-22 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodApp', '0009_adminbloodrequest_p_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminbloodrequest',
            name='p_location',
            field=models.CharField(default='', max_length=100),
        ),
    ]
