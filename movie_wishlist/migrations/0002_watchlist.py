# Generated by Django 2.0.4 on 2018-05-02 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_wishlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('actor', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
            ],
        ),
    ]
