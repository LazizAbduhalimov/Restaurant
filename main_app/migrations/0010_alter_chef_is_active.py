# Generated by Django 3.2.4 on 2021-08-04 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20210804_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активность'),
        ),
    ]