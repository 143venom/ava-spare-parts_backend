# Generated by Django 5.1 on 2024-09-11 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogs',
            options={'verbose_name_plural': 'Blog'},
        ),
        migrations.AlterField(
            model_name='blogs',
            name='slug',
            field=models.SlugField(blank=True, default='Slug Will Auto Generate', max_length=255, unique=True, verbose_name='Blog Slug'),
        ),
    ]
