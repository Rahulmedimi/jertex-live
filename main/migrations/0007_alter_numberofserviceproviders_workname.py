# Generated by Django 4.0.4 on 2022-04-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_numberofserviceproviders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberofserviceproviders',
            name='workname',
            field=models.CharField(max_length=50),
        ),
    ]
