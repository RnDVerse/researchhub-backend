# Generated by Django 2.2.9 on 2020-02-13 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0018_auto_20200213_2311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='is_censored',
            new_name='is_removed',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='is_censored',
            new_name='is_removed',
        ),
        migrations.RenameField(
            model_name='thread',
            old_name='is_censored',
            new_name='is_removed',
        ),
    ]