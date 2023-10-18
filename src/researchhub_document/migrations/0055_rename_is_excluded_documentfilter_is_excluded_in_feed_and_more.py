# Generated by Django 4.1 on 2023-10-18 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("researchhub_document", "0054_researchhubunifieddocument_concepts"),
    ]

    operations = [
        migrations.RenameField(
            model_name="documentfilter",
            old_name="is_excluded",
            new_name="is_excluded_in_feed",
        ),
        migrations.AddField(
            model_name="documentfilter",
            name="is_excluded_in_hubs",
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
