# Generated by Django 3.2 on 2021-05-16 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_noticia_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='video',
        ),
        migrations.AddField(
            model_name='noticia',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='noticias'),
        ),
    ]