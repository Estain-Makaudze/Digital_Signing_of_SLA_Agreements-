# Generated by Django 3.2.1 on 2021-08-04 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_agre', '0020_auto_20210804_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agreemnets',
            name='date_signed',
        ),
    ]