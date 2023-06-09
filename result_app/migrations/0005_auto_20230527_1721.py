# Generated by Django 3.2.18 on 2023-05-27 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result_app', '0004_alter_result_stud_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='result',
            options={'ordering': ['-date_posted']},
        ),
        migrations.AddField(
            model_name='fee',
            name='month_paid',
            field=models.CharField(blank=True, choices=[('JANUARY', 'JANUARY'), ('FEBRUARY', 'FEBRUARY'), ('MARCH', 'MARCH'), ('APRIL', 'APRIL'), ('MAY', 'MAY'), ('JUNE', 'JUNE'), ('JULY', 'JULY'), ('AUGUST', 'AUGUST'), ('SEPTEMBER', 'SEPTEMBER'), ('OCTOBER', 'OCTOBER'), ('NOVEMBER', 'NOVEMBER'), ('DECEMBER', 'DECEMBER')], max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='fee',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
