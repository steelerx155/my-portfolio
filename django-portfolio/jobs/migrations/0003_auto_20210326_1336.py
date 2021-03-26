# Generated by Django 3.1.7 on 2021-03-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20210325_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='github_url',
            field=models.URLField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='heroku_url',
            field=models.URLField(max_length=100, null=True),
        ),
    ]
