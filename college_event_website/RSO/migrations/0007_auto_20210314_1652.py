# Generated by Django 3.1.6 on 2021-03-14 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSO', '0006_rso_total_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rso',
            name='total_students',
            field=models.IntegerField(default=5),
        ),
    ]
