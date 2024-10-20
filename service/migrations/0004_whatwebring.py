# Generated by Django 5.1 on 2024-09-11 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_services_options_alter_services_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatWeBring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='whatwebring/images/', verbose_name='WhatWeBring Image')),
                ('title', models.CharField(max_length=255, verbose_name='WhatWeBring Name')),
                ('description', models.TextField(verbose_name='WhatWeBring Description')),
            ],
        ),
    ]