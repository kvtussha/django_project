# Generated by Django 5.0 on 2024-02-02 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_remove_mailinglog_mailing_remove_client_mailing_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productversion',
            name='current_version',
        ),
        migrations.AddField(
            model_name='productversion',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='статус версии'),
        ),
    ]
