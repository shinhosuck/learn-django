# Generated by Django 3.1 on 2020-12-17 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postlike'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostLike',
        ),
    ]