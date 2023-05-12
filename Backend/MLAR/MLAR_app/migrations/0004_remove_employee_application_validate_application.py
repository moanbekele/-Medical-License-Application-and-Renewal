# Generated by Django 4.2 on 2023-05-05 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MLAR_app', '0003_alter_application_applicant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='application',
        ),
        migrations.AddField(
            model_name='validate',
            name='application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MLAR_app.application'),
        ),
    ]