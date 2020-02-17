# Generated by Django 2.2 on 2020-02-15 03:08

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_auto_20200211_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号')),
            ],
            options={
                'verbose_name': '用户模型',
                'verbose_name_plural': '用户模型类',
                'db_table': '用户类',
                'ordering': ['telephone'],
            },
            managers=[
                ('manage', django.db.models.manager.Manager()),
            ],
        ),
    ]