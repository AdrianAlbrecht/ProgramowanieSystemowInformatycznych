# Generated by Django 3.2.9 on 2022-01-05 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccinationProject', '0002_auto_20220105_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='visit_time',
            field=models.TimeField(blank=True, default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='visit_date',
            field=models.DateField(blank=True, default='1000-01-01'),
        ),
    ]
