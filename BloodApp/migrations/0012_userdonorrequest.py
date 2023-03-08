# Generated by Django 4.1.7 on 2023-02-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodApp', '0011_alter_adminbloodrequest_p_age_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDonorRequest',
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
