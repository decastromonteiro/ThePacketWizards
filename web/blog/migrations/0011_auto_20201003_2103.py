# Generated by Django 3.1.1 on 2020-10-04 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20201003_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitterpost',
            name='post_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='twitter_content',
            field=models.TextField(blank=True, max_length=257, null=True),
        ),
        migrations.AlterField(
            model_name='twitterpost',
            name='content',
            field=models.TextField(blank=True, max_length=257, null=True),
        ),
    ]
