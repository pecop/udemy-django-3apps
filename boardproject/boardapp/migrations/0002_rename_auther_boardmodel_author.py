# Generated by Django 3.2.3 on 2021-05-24 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boardmodel',
            old_name='auther',
            new_name='author',
        ),
    ]