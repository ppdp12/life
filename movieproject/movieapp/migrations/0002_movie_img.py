# Generated by Django 3.2.9 on 2021-12-06 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='dddhs', upload_to='galary'),
            preserve_default=False,
        ),
    ]
