# Generated by Django 3.0.7 on 2020-12-30 04:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_auto_20201230_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postlike',
            name='post',
        ),
        migrations.AddField(
            model_name='postlike',
            name='post',
            field=models.ManyToManyField(to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='postlike',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
