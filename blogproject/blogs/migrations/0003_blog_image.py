# Generated by Django 3.0.1 on 2020-04-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20200401_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='static/img/noimg.jpg', upload_to='static/img/'),
        ),
    ]
