# Generated by Django 3.0.3 on 2020-03-28 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200215_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='picname',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='picurl',
            field=models.TextField(default='-'),
        ),
    ]
