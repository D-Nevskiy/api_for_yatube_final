# Generated by Django 3.2.3 on 2022-11-18 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_follow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
    ]
