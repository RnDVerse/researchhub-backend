# Generated by Django 2.2 on 2022-07-21 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0052_auto_20220721_0356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='discussion_type',
            new_name='discussion_post_type',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='discussion_type',
            new_name='discussion_post_type',
        ),
        migrations.RenameField(
            model_name='thread',
            old_name='discussion_type',
            new_name='discussion_post_type',
        ),
    ]
