# Generated by Django 2.2.12 on 2020-05-28 13:09

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('Title', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('image', models.ImageField(default=None, null=True, upload_to='news')),
                ('news_body', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]
