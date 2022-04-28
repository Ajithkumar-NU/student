# Generated by Django 4.0.3 on 2022-04-12 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_employee_image_alter_employee_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='eid',
            field=models.IntegerField(primary_key=b'I01\n', serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
