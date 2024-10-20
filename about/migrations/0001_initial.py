# Generated by Django 5.1 on 2024-09-11 06:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The main title for the About section.', max_length=255, verbose_name='Title')),
                ('subtitle', models.CharField(help_text='The subtitle for the About section.', max_length=255, verbose_name='Subtitle')),
                ('description', ckeditor.fields.RichTextField(help_text='A detailed description of the About section.', verbose_name='Description')),
                ('image', models.ImageField(help_text='Upload an image for the About section.', upload_to='about/about/', verbose_name='Image')),
            ],
            options={
                'verbose_name_plural': 'About',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='AboutList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title for the About List.', max_length=255, verbose_name='Title')),
            ],
            options={
                'verbose_name_plural': 'About List',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(help_text='The name of the team member.', max_length=255, verbose_name='Name')),
                ('profession', models.CharField(help_text='The profession or role of the team member.', max_length=255, verbose_name='Profession')),
                ('description', ckeditor.fields.RichTextField(help_text='A description of the team member.', verbose_name='Description')),
                ('image', models.ImageField(help_text='Upload an image of the team member.', upload_to='about/team/', verbose_name='Image')),
            ],
            options={
                'verbose_name_plural': 'Team Member',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('position', models.CharField(blank=True, max_length=255, null=True, verbose_name='Position')),
                ('testimonial', models.TextField(verbose_name='Testimonial')),
                ('image', models.ImageField(blank=True, null=True, upload_to='testimonials/', verbose_name='Image')),
                ('rating', models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')], verbose_name='Rating')),
            ],
            options={
                'verbose_name_plural': 'Testimonials',
                'ordering': ['-posted_at'],
            },
        ),
    ]