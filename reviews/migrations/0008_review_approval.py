# Generated by Django 4.0.5 on 2022-10-31 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_remove_review_one_review_per_user_per_game_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='approval',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Denied', 'Denied')], default='Denied', max_length=8),
        ),
    ]