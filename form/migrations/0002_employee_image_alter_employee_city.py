# Generated by Django 4.0.3 on 2022-04-11 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.CharField(default='ajmer', max_length=20),
        ),
    ]
