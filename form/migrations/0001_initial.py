# Generated by Django 4.0.3 on 2022-04-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.CharField(max_length=40, primary_key=b'I01\n', serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('city', models.CharField(default='delhi', max_length=20)),
                ('gender', models.CharField(default='male', max_length=20)),
                ('vehicles', models.CharField(default='Car', max_length=20)),
            ],
        ),
    ]
