# Generated by Django 4.1 on 2024-05-22 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0112_alter_author_orcid_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="authorinstitution",
            name="is_primary",
        ),
    ]
