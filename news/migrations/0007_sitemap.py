# Generated by Django 2.2.12 on 2020-07-31 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200709_0935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sitemap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitemap_value', models.TextField()),
            ],
        ),
    ]