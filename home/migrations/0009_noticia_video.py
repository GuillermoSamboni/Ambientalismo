# Generated by Django 3.2 on 2021-05-16 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210515_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='video_noticas'),
        ),
    ]
