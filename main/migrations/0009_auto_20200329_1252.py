# Generated by Django 3.0.3 on 2020-03-29 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200328_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='picname2',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='picurl2',
            field=models.TextField(default='-'),
        ),
    ]
