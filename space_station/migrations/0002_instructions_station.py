# Generated by Django 4.1.3 on 2022-11-23 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('space_station', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructions',
            name='station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='space_station.station'),
        ),
    ]
