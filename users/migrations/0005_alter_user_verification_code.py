# Generated by Django 5.0.2 on 2024-02-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_verification_code_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(max_length=8),
        ),
    ]