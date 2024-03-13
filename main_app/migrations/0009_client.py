# Generated by Django 5.0 on 2024-01-23 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_post_is_published_alter_post_views_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='client name')),
                ('email', models.EmailField(max_length=254)),
                ('product_id', models.IntegerField(blank=True, null=True, verbose_name='product id')),
                ('post_id', models.IntegerField(blank=True, null=True, verbose_name='post id')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
                'ordering': ('name',),
            },
        ),
    ]