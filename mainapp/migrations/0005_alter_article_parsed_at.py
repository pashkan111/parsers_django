# Generated by Django 3.2.5 on 2021-07-26 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210725_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='parsed_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время парсинга'),
        ),
    ]
