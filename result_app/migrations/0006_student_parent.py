# Generated by Django 3.2.18 on 2023-05-29 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result_app', '0005_auto_20230527_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
