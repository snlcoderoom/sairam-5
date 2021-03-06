# Generated by Django 3.2.8 on 2022-03-25 03:01

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_sivam_about_page_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sivam_ew_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sivam_img', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('write_up', ckeditor.fields.RichTextField()),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Sivam_spw_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sivam_img', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('write_up', ckeditor.fields.RichTextField()),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Sivam_srw_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sivam_img', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('write_up', ckeditor.fields.RichTextField()),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
