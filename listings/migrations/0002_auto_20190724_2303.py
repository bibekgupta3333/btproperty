# Generated by Django 2.2.1 on 2019-07-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='sqft',
            field=models.IntegerField(default=0),
        ),
    ]
