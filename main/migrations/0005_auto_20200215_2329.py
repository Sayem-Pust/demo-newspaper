# Generated by Django 3.0.2 on 2020-02-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_main_set_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='link',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='tell',
            field=models.TextField(default='-'),
        ),
    ]