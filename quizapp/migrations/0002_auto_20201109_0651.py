# Generated by Django 3.1.2 on 2020-11-09 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizform',
            name='questions',
            field=models.TextField(max_length=100),
        ),
    ]