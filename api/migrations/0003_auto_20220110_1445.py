# Generated by Django 3.0.8 on 2022-01-10 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220110_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdb',
            old_name='zip',
            new_name='zip_code',
        ),
    ]
