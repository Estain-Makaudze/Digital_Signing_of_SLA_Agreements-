# Generated by Django 3.2.1 on 2021-06-14 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0005_confirm_fill'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirm_fill',
            name='Asigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asigned_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='confirm_fill',
            name='Room_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_owen', to=settings.AUTH_USER_MODEL),
        ),
    ]
