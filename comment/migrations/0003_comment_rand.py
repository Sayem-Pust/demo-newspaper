# Generated by Django 3.0.2 on 2020-04-26 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_comment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rand',
            field=models.IntegerField(default=0),
        ),
    ]
