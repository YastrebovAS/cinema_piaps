# Generated by Django 4.2 on 2023-10-19 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_alter_articles_path_alter_films_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 10, 19, 19, 50, 57, 758967)),
        ),
    ]