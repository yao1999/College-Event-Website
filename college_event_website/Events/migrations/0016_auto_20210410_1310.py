# Generated by Django 3.1.7 on 2021-04-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0015_auto_20210410_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.TimeField(default='13:10:31'),
        ),
    ]
