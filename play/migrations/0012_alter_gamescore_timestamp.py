# Generated by Django 4.0.5 on 2022-10-18 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0011_gamescore_word_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamescore',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]