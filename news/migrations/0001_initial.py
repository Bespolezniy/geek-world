# Generated by Django 3.0.2 on 2020-01-16 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique_for_date='date', verbose_name='New title')),
                ('description', models.TextField(verbose_name='Short content')),
                ('content', models.TextField(verbose_name='All information')),
                ('date', models.DateField(db_index=True, default=datetime.datetime(2020, 1, 16, 15, 58, 3, 237248), verbose_name='Published')),
            ],
            options={
                'verbose_name': 'new',
                'verbose_name_plural': 'news',
                'ordering': ['-date'],
            },
        ),
    ]
