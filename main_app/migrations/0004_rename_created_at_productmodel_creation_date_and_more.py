# Generated by Django 5.0 on 2023-12-27 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_creation_date_productmodel_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmodel',
            old_name='created_at',
            new_name='creation_date',
        ),
        migrations.RenameField(
            model_name='productmodel',
            old_name='updated_at',
            new_name='last_modified_date',
        ),
    ]