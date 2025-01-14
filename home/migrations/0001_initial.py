# Generated by Django 5.1 on 2024-09-11 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the Brane company', max_length=255, verbose_name='company name')),
                ('image', models.ImageField(upload_to='home/brand/')),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='Active', help_text='Status of the Brand', max_length=8)),
            ],
            options={
                'verbose_name_plural': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='CompanyHighlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='home/companyhighlight/')),
                ('title', models.CharField(max_length=255, verbose_name='company highlight title')),
                ('number', models.CharField(max_length=255, verbose_name='company highlight title')),
            ],
            options={
                'verbose_name_plural': 'Company Highlight',
            },
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
        migrations.CreateModel(
            name='FeedBackForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the person giving feedback', max_length=255, verbose_name='Full Name')),
                ('email', models.EmailField(help_text='Email address of the person giving feedback', max_length=255, verbose_name='Email Address')),
                ('phone', models.CharField(help_text='Phone number of the person giving feedback', max_length=20, verbose_name='Phone Number')),
                ('subject', models.CharField(help_text='Subject of the feedback', max_length=255, verbose_name='Subject')),
                ('message', models.CharField(help_text='Message of the feedback', max_length=255, verbose_name='Message')),
            ],
            options={
                'verbose_name_plural': 'Feedback Form',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the main title for the slider.', max_length=255, verbose_name='Title')),
                ('sub_title', models.CharField(help_text='Enter the subtitle for the slider.', max_length=255, verbose_name='Subtitle')),
                ('image', models.ImageField(default='default/default_slider.jpeg', help_text='Upload an image for the slider. Default image will be used if none is provided.', upload_to='home/sliders/', verbose_name='Slider Image')),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='Active', help_text='Status of the Slider', max_length=8)),
            ],
            options={
                'verbose_name_plural': 'Slider',
            },
        ),
    ]
