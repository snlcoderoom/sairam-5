# Generated by Django 3.2.8 on 2022-03-29 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0041_register_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('samithi', models.CharField(blank=True, choices=[('Ameerpet', 'Ameerpet'), ('Amberpet', 'Amberpet'), ('Dilsukhnagar', 'Dilsukhnagar'), ('Gandhinagar', 'Gandhinagar'), ('Himayathnagar', 'Himayathnagar'), ('Kachiguda', 'Kachiguda'), ('Khairtabad', 'Khairtabad'), ('Koti', 'Koti'), ('Mehdipatnam', 'Mehdipatnam'), ('Marredpally', 'Marredpally'), ('Prasanthi Nagar', 'Prasanthi Nagar'), ('Seethaphalmandi', 'Seethaphalmandi'), ('S R Nagar', 'S R Nagar'), ('Tarnaka', 'Tarnaka'), ('Vengal Rao Nagar', 'Vengal Rao Nagar'), ('Vidya Nagar', 'Vidya Nagar')], max_length=50)),
                ('mobile', models.IntegerField(null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('reg', models.CharField(max_length=30, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
