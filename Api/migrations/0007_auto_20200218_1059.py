# Generated by Django 3.0.3 on 2020-02-18 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0006_auto_20200218_1045'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Branches',
            new_name='Branch',
        ),
    ]