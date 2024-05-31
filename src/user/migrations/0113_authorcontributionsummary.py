# Generated by Django 4.1 on 2024-05-22 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0112_alter_author_orcid_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthorContributionSummary",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "source",
                    models.CharField(
                        choices=[
                            ("OPENALEX", "OpenAlex"),
                            ("RESEARCHHUB", "ResearchHub"),
                        ],
                        max_length=20,
                    ),
                ),
                ("works_count", models.IntegerField(blank=True, null=True)),
                ("citation_count", models.IntegerField(blank=True, null=True)),
                ("year", models.IntegerField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contribution_summaries",
                        to="user.author",
                    ),
                ),
            ],
            options={
                "unique_together": {("source", "author", "year")},
            },
        ),
    ]