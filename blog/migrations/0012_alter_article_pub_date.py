# Generated by Django 3.2.6 on 2021-08-23 07:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Время публикации'),
        ),
    ]
