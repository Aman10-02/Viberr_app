# Generated by Django 4.0.3 on 2022-04-12 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_album_album_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(max_length=10000, upload_to=''),
        ),
    ]
