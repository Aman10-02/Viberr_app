# Generated by Django 4.0.3 on 2022-04-12 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.CharField(max_length=10000),
        ),
    ]
