# Generated by Django 2.2.6 on 2019-11-01 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_auto_20191101_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.CharField(max_length=255, verbose_name='文章描述'),
        ),
    ]
