# Generated by Django 3.2.1 on 2021-07-04 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_agre', '0013_alter_agreemnets_signed_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreemnets',
            name='Signed_pdf',
            field=models.FileField(blank=True, null=True, upload_to='base/media'),
        ),
    ]
