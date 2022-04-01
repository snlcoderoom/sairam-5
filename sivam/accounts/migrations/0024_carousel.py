# Generated by Django 3.2.8 on 2022-03-20 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20220320_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics/%y/%m/%d/')),
                ('title', models.CharField(max_length=150)),
                ('action_name', models.CharField(max_length=50)),
                ('link', models.TextField(blank=True, null=True)),
                ('sub_title', models.CharField(max_length=100)),
            ],
        ),
    ]