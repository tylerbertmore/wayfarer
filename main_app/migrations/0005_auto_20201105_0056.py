# Generated by Django 3.1.2 on 2020-11-05 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20201103_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]