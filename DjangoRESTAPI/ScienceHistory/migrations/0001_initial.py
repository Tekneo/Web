# Generated by Django 3.1 on 2020-08-26 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sciencehistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scientist_name', models.CharField(max_length=10)),
                ('scientist_DOB', models.IntegerField()),
                ('science_discovery', models.CharField(max_length=10)),
                ('scientist_DOD', models.IntegerField()),
            ],
        ),
    ]