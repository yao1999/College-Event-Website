# Generated by Django 3.1.6 on 2021-03-11 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0010_auto_20210311_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.TimeField(default='11:15:25'),
        ),
    ]
