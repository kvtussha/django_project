# Generated by Django 5.0 on 2024-01-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_rename_blogpost_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='статус публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='views_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='кол-во просмотров'),
        ),
    ]
