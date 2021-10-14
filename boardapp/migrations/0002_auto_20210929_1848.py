# Generated by Django 3.2.7 on 2021-09-29 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardmodel',
            name='title',
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='good',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='read',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='readtext',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='sns_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
