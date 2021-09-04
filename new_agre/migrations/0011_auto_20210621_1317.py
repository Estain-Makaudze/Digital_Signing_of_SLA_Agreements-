# Generated by Django 3.2.1 on 2021-06-21 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_agre', '0010_auto_20210620_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_cont_form',
            name='Client_performance_review',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='client_cont_form',
            name='Customer_Requirement1',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='client_cont_form',
            name='Customer_Requirement2',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='client_cont_form',
            name='Customer_Requirement3',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='service_cont_form',
            name='Goal_of_sla',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='service_cont_form',
            name='Perfomace_review_frequency',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='service_cont_form',
            name='Purpose_of_sla',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='service_cont_form',
            name='Service_Detailed_description1',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='service_cont_form',
            name='Service_Detailed_description2',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='service_cont_form',
            name='Service_Detailed_description3',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='service_cont_form',
            name='Service_Detailed_description4',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='service_cont_form',
            name='Service_provider_requirement1',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='service_cont_form',
            name='Service_provider_requirement2',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='service_cont_form',
            name='Service_provider_requirement3',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='service_cont_form',
            name='Service_provider_requirement4',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='service_cont_form',
            name='Service_to_supply',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='service_cont_form',
            name='Sla_objectives1',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='service_cont_form',
            name='Sla_objectives2',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='service_cont_form',
            name='Sla_objectives3',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='service_cont_form',
            name='Sla_objectives4',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
    ]