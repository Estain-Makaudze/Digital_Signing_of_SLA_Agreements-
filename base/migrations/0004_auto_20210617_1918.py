# Generated by Django 3.2.1 on 2021-06-17 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_pdf_pdf1'),
    ]

    operations = [
        migrations.CreateModel(
            name='YourModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=120)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdfs/')),
            ],
            options={
                'verbose_name_plural': 'PDF',
            },
        ),
        migrations.DeleteModel(
            name='pdf1',
        ),
    ]
