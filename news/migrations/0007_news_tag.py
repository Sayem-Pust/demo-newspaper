# Generated by Django 3.0.3 on 2020-03-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200324_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.TextField(default=''),
        ),
    ]
