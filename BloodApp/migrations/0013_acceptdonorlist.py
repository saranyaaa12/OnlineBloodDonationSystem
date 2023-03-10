# Generated by Django 4.1.7 on 2023-02-23 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodApp', '0012_userdonorrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptDonorList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_name', models.CharField(default='', max_length=30)),
                ('d_age', models.CharField(default='', max_length=5)),
                ('d_gender', models.CharField(default='', max_length=10)),
                ('d_contact', models.CharField(default='', max_length=12)),
                ('d_bloodgroup', models.CharField(default='', max_length=5)),
                ('d_healthissues', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
