# Generated by Django 3.0.7 on 2020-06-28 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='liked',
            field=models.BooleanField(default=False),
        ),
    ]
