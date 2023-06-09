# Generated by Django 4.2 on 2023-05-06 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MLAR_app', '0009_regain_lost_license_id_serial_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='first_license_application',
            name='declination_reason',
            field=models.CharField(choices=[('Forgery', 'Forgery'), ('Low Quality Documents', 'Low Quality Documents'), ('Invalid Credentials', 'Invalid Credentials')], max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='first_license_application',
            name='validation_status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Declined', 'Declined')], max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='regain_lost_license',
            name='declination_reason',
            field=models.CharField(choices=[('Forgery', 'Forgery'), ('Low Quality Documents', 'Low Quality Documents'), ('Invalid Credentials', 'Invalid Credentials')], max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='regain_lost_license',
            name='validation_status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Declined', 'Declined')], max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='renew_last_license',
            name='declination_reason',
            field=models.CharField(choices=[('Forgery', 'Forgery'), ('Low Quality Documents', 'Low Quality Documents'), ('Invalid Credentials', 'Invalid Credentials')], max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='renew_last_license',
            name='validation_status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Declined', 'Declined')], max_length=500, null=True),
        ),
    ]
