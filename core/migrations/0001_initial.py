# Generated by Django 3.0.7 on 2020-06-28 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordem', models.IntegerField(unique=True)),
                ('img', models.ImageField(upload_to='static/pages/')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=10)),
                ('ip', models.CharField(max_length=10)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Page')),
            ],
        ),
    ]