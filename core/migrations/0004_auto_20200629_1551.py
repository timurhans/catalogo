# Generated by Django 3.0.7 on 2020-06-29 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200628_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='cnpj',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='like',
            name='ip',
            field=models.CharField(max_length=30),
        ),
    ]
