# Generated by Django 3.2.6 on 2021-08-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_agre', '0024_agreemnets_real_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='agree_edits',
            name='Contr_Dig_sig',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='agreemnets',
            name='Contr_Dig_sig',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
