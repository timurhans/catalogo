# Generated by Django 3.0.7 on 2020-06-28 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_like_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='img',
            field=models.FileField(upload_to='static/pages/'),
        ),
    ]