# Generated by Django 4.2 on 2023-05-06 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MLAR_app', '0007_remove_first_license_application_serial_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='first_license_application',
            name='id_serial_no',
            field=models.CharField(max_length=36, null=True),
        ),
        migrations.AlterField(
            model_name='renew_last_license',
            name='id_serial_no',
            field=models.CharField(max_length=36, null=True),
        ),
    ]