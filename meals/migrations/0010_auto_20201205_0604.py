# Generated by Django 2.1.5 on 2020-12-05 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0009_auto_20201205_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='description',
            field=models.CharField(max_length=2000),
        ),
    ]