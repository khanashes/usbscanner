# Generated by Django 4.1.4 on 2022-12-13 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.CharField(max_length=1000)),
                ('filePath', models.CharField(max_length=1000)),
                ('total_score', models.CharField(max_length=1000)),
                ('fileType', models.CharField(max_length=1000)),
                ('fileSize', models.CharField(max_length=1000)),
                ('firstBytesString', models.CharField(max_length=1000)),
                ('hashString', models.CharField(max_length=1000)),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]