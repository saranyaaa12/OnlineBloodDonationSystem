# Generated by Django 4.1.7 on 2023-02-24 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodApp', '0015_acceptbloodlist_rejectbloodlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdonorrequest',
            name='d_location',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='userdonorrequest',
            name='d_visit',
            field=models.CharField(default='', max_length=5),
        ),
    ]
