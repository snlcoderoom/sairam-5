# Generated by Django 3.2.9 on 2021-11-15 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20211115_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='report',
            name='pahoto1',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='report',
            name='pahoto2',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]