# Generated by Django 4.0.4 on 2022-05-27 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahsulot', '0009_footermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appstore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('app_store', models.CharField(max_length=200)),
                ('google_play', models.CharField(max_length=200)),
            ],
        ),
    ]
