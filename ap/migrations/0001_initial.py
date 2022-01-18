# Generated by Django 3.2 on 2022-01-15 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_details_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('number', models.IntegerField(unique=True)),
                ('date_time', models.DateTimeField()),
                ('patient_id', models.CharField(default='string', max_length=10)),
            ],
        ),
    ]
