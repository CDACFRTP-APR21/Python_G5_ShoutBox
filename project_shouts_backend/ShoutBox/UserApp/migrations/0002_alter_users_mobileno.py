# Generated by Django 3.2.3 on 2021-06-14 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='MobileNo',
            field=models.BigIntegerField(),
        ),
    ]
