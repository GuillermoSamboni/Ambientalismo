# Generated by Django 3.2 on 2021-05-16 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_noticia_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='video_noticas'),
        ),
    ]
