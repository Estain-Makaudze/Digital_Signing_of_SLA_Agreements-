# Generated by Django 3.2.1 on 2021-06-20 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_agre', '0007_agree_edits_agreement_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agree_edits',
            name='Signed_pdf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Agrep', to='new_agre.agreemnets'),
        ),
    ]
