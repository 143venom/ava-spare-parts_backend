# Generated by Django 5.1 on 2024-09-11 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_services_options_alter_services_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name_plural': 'Services'},
        ),
        migrations.AlterField(
            model_name='services',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Service Slug'),
        ),
    ]