# Generated by Django 3.2.9 on 2021-12-03 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seance',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Slug'),
        ),
    ]
