# Generated by Django 3.0.2 on 2020-02-15 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200215_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]