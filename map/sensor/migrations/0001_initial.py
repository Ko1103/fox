# Generated by Django 2.1.4 on 2019-01-26 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_name', models.CharField(max_length=15)),
                ('value', models.FloatField()),
                ('temp_value', models.FloatField()),
                ('create_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_name', models.CharField(max_length=15)),
                ('value', models.FloatField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
