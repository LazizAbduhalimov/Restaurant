# Generated by Django 3.2.4 on 2021-08-04 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20210804_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chef',
            old_name='is_accept',
            new_name='is_active',
        ),
    ]
