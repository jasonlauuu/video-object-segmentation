# Generated by Django 2.2.6 on 2019-11-22 04:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='headFile',
        ),
        migrations.AddField(
            model_name='video',
            name='File',
            field=models.FileField(default=0, upload_to='./upload/File'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='Frame',
            field=models.FileField(default=django.utils.timezone.now, upload_to='./upload/First_Frame'),
            preserve_default=False,
        ),
    ]
