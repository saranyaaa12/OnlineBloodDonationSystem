# Generated by Django 4.1.7 on 2023-02-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodApp', '0008_adminbloodrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminbloodrequest',
            name='p_contact',
            field=models.CharField(default='', max_length=12),
        ),
    ]
