# Generated by Django 2.2 on 2020-02-25 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20200225_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author_img',
            field=models.ImageField(default=0, upload_to='author_imgs', verbose_name='作者头像'),
        ),
    ]
