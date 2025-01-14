# Generated by Django 5.1 on 2024-09-11 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('first_name', models.CharField(help_text='First Name of the sender', max_length=100, verbose_name='First Name')),
                ('second_name', models.CharField(help_text='Second Name of the sender', max_length=100, verbose_name='Second Name')),
                ('email', models.EmailField(help_text="Sender's email address", max_length=254, verbose_name='Email Address')),
                ('message', models.TextField(help_text='The message content', verbose_name='Message')),
            ],
            options={
                'verbose_name_plural': 'Contact Form Entries',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_iframe', models.TextField(blank=True, help_text='Embed code for Google Maps', null=True, verbose_name='Google Maps Iframe')),
            ],
            options={
                'verbose_name_plural': 'Map',
            },
        ),
    ]
