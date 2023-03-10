# Generated by Django 4.1.7 on 2023-02-18 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=5)),
                ('gender', models.CharField(default='', max_length=10)),
                ('password', models.CharField(max_length=30)),
                ('blood', models.CharField(default='', max_length=5)),
                ('phone', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=10)),
                ('health', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=6)),
            ],
        ),
    ]
