# Generated by Django 4.2.11 on 2024-05-29 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(default='body'),
        ),
    ]
