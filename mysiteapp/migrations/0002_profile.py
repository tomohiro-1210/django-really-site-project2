# Generated by Django 5.1.1 on 2024-09-12 07:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysiteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('username', models.CharField(default='匿名ユーザー', max_length=30)),
                ('zipcode', models.CharField(default='', max_length=10)),
                ('prefecture', models.CharField(default='', max_length=6)),
                ('city', models.CharField(default='', max_length=10)),
                ('address', models.CharField(default='', max_length=150)),
            ],
        ),
    ]
