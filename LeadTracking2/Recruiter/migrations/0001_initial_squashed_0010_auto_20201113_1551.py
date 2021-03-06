# Generated by Django 3.1.2 on 2020-11-17 15:51

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    replaces = [('Recruiter', '0001_initial'), ('Recruiter', '0002_auto_20201102_1726'), ('Recruiter', '0003_auto_20201102_2030'), ('Recruiter', '0004_auto_20201108_2026'), ('Recruiter', '0005_student_country'), ('Recruiter', '0006_auto_20201112_1235'), ('Recruiter', '0007_auto_20201112_1249'), ('Recruiter', '0008_auto_20201113_1519'), ('Recruiter', '0009_auto_20201113_1520'), ('Recruiter', '0010_auto_20201113_1551')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=40)),
                ('MiddleName', models.CharField(blank=True, max_length=40)),
                ('LastName', models.CharField(max_length=40)),
                ('Email', models.CharField(blank=True, max_length=30)),
                ('PhoneNumber', models.CharField(max_length=50)),
                ('Status', models.IntegerField(default=1)),
                ('StatusChangedBy', models.CharField(max_length=100)),
                ('UserSavedBy', models.IntegerField(default=0)),
                ('country', django_countries.fields.CountryField(max_length=746, multiple=True)),
            ],
        ),
    ]
