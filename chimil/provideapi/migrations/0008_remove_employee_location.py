# Generated by Django 3.0.2 on 2020-02-05 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provideapi', '0007_employee_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='location',
        ),
    ]
