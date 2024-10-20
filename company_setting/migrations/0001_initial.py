# Generated by Django 5.1 on 2024-09-11 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(help_text='The full name of the company', max_length=255, verbose_name='Company Name')),
                ('email', models.EmailField(help_text='The main contact email for the company', max_length=254, verbose_name='Email Address')),
                ('phone', models.CharField(help_text='The main contact phone number for the company', max_length=15, verbose_name='Phone Number')),
                ('address', models.CharField(blank=True, default='Your Address', help_text='The street address of the company', max_length=700, null=True, verbose_name='Street Address')),
                ('city', models.CharField(blank=True, default='Your City', help_text='The city where the company is located', max_length=200, null=True, verbose_name='City')),
                ('state', models.CharField(blank=True, default='Your State', help_text='The state or province where the company is located', max_length=200, null=True, verbose_name='State/Province')),
                ('postal', models.IntegerField(blank=True, default=12345, help_text="The postal code for the company's location", null=True, verbose_name='Postal Code')),
                ('country', models.CharField(blank=True, default='Your Country', help_text='The country where the company is located', max_length=300, null=True, verbose_name='Country')),
                ('day', models.CharField(default='Monday - Friday', help_text='Day of the week for the opening hours', max_length=9, verbose_name='Day of the Week')),
                ('opening_hours', models.CharField(default='10 am - 8 pm', help_text="Company's regular opening hours", max_length=100, verbose_name='Opening Hours')),
            ],
            options={
                'verbose_name_plural': 'Company Information',
            },
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copyright', models.CharField(blank=True, help_text='The copyright notice to display in the footer', max_length=500, null=True, verbose_name='Copyright Text')),
            ],
            options={
                'verbose_name_plural': 'Footer',
            },
        ),
        migrations.CreateModel(
            name='SiteLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, default='default/favicon.ico', help_text='Upload the logo of the company', null=True, upload_to='company/logo/', verbose_name='Company Logo')),
                ('favicon', models.ImageField(blank=True, default='default/favicon.ico', help_text='Upload the favicon for the website', null=True, upload_to='company/logo/', verbose_name='Favicon')),
            ],
            options={
                'verbose_name_plural': 'Site Logo',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, help_text="URL to the company's Facebook page", max_length=255, null=True, verbose_name='Facebook URL')),
                ('twitter', models.URLField(blank=True, help_text="URL to the company's Twitter profile", max_length=255, null=True, verbose_name='Twitter URL')),
                ('linkedin', models.URLField(blank=True, help_text="URL to the company's LinkedIn profile", max_length=255, null=True, verbose_name='LinkedIn URL')),
                ('instagram', models.URLField(blank=True, help_text="URL to the company's Instagram profile", max_length=255, null=True, verbose_name='Instagram URL')),
                ('youtube', models.URLField(blank=True, help_text="URL to the company's YouTube channel", max_length=255, null=True, verbose_name='YouTube Channel URL')),
            ],
            options={
                'verbose_name_plural': 'Social Media',
            },
        ),
    ]
