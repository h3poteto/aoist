# Generated by Django 2.0.1 on 2018-01-22 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=255)),
                ('thumbnail', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
        ),
    ]
