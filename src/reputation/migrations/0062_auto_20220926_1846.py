# Generated by Django 2.2 on 2022-09-26 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0061_bounty_unified_document'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='contribution',
            index=models.Index(fields=['content_type', 'object_id'], name='reputation__content_9e536b_idx'),
        ),
    ]