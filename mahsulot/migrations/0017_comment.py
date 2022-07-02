# Generated by Django 4.0.4 on 2022-05-27 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahsulot', '0016_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nick_name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='Media/comment_img')),
            ],
        ),
    ]