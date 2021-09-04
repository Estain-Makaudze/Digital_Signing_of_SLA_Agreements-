# Generated by Django 3.2.1 on 2021-08-04 17:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('new_agre', '0018_auto_20210804_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agree_edits',
            old_name='date_signed',
            new_name='date_Client_sign',
        ),
        migrations.RemoveField(
            model_name='agreemnets',
            name='date_Client_sign',
        ),
        migrations.RemoveField(
            model_name='agreemnets',
            name='date_Service_prov_sign',
        ),
        migrations.AddField(
            model_name='agree_edits',
            name='date_Service_prov_sign',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
