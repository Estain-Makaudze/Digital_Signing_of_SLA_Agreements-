# Generated by Django 3.2.1 on 2021-06-19 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_agre', '0004_auto_20210619_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreemnets',
            name='Dig_sig',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='agreemnets',
            name='Private_key',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='agreemnets',
            name='Public_key',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
