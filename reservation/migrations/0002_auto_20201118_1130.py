# Generated by Django 2.1.5 on 2020-11-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='Date',
            field=models.DateField(verbose_name='2020-11-16'),
        ),
    ]
