# Generated by Django 3.2.6 on 2021-08-23 07:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 23, 12, 18, 29, 606974), verbose_name='Время публикации'),
        ),
    ]