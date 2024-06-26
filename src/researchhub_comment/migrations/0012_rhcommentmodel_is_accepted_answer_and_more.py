# Generated by Django 4.1 on 2023-03-17 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "researchhub_comment",
            "0011_rhcommentmodel_is_public_rhcommentmodel_is_removed_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="rhcommentmodel",
            name="is_accepted_answer",
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name="rhcommentthreadmodel",
            name="thread_type",
            field=models.CharField(
                choices=[
                    ("GENERIC_COMMENT", "GENERIC_COMMENT"),
                    ("INNER_CONTENT_COMMENT", "INNER_CONTENT_COMMENT"),
                    ("ANSWER", "ANSWER"),
                    ("REVIEW", "REVIEW"),
                    ("SUMMARY", "SUMMARY"),
                ],
                default="GENERIC_COMMENT",
                max_length=144,
            ),
        ),
    ]
