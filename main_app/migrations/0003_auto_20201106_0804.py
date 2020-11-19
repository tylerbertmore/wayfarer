# Generated by Django 3.1.2 on 2020-11-06 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201106_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='posts/images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_image',
            field=models.ImageField(null=True, upload_to='user/images'),
        ),
    ]