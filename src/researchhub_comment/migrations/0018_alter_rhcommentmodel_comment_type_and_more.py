# Generated by Django 4.1 on 2023-12-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("researchhub_comment", "0017_rhcommentmodel_comment_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rhcommentmodel",
            name="comment_type",
            field=models.CharField(
                choices=[
                    ("GENERIC_COMMENT", "GENERIC_COMMENT"),
                    ("INNER_CONTENT_COMMENT", "INNER_CONTENT_COMMENT"),
                    ("ANSWER", "ANSWER"),
                    ("REVIEW", "REVIEW"),
                    ("SUMMARY", "SUMMARY"),
                    ("REPLICABILITY_COMMENT", "REPLICABILITY_COMMENT"),
                ],
                default="GENERIC_COMMENT",
                max_length=144,
            ),
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
                    ("REPLICABILITY_COMMENT", "REPLICABILITY_COMMENT"),
                ],
                default="GENERIC_COMMENT",
                max_length=144,
            ),
        ),
    ]
