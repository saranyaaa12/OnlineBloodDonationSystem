# Generated by Django 4.1.7 on 2023-02-25 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodApp', '0019_rejectdonorlist_d_location_rejectdonorlist_d_visit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdonorrequest',
            name='d_gender',
            field=models.CharField(default='+91', max_length=10),
        ),
    ]