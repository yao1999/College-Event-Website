# Generated by Django 3.1.6 on 2021-03-24 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0004_auto_20210323_2041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locations',
            old_name='name',
            new_name='location_name',
        ),
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.TimeField(default='17:11:58'),
        ),
    ]
