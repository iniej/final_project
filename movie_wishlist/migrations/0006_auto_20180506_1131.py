# Generated by Django 2.0.4 on 2018-05-06 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_wishlist', '0005_auto_20180503_2041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchedlist',
            old_name='title',
            new_name='name',
        ),
    ]
