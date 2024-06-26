# Generated by Django 4.1 on 2024-05-17 20:27

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("institution", "0004_institution_openalex_created_date_and_more"),
        ("user", "0105_remove_author_academic_verification_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthorInstitution",
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
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "years",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(),
                        blank=True,
                        default=list,
                        size=None,
                    ),
                ),
                ("is_primary", models.BooleanField(default=False)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="institutions",
                        to="user.author",
                    ),
                ),
                (
                    "institution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="author_institutions",
                        to="institution.institution",
                    ),
                ),
            ],
            options={
                "unique_together": {("author", "institution")},
            },
        ),
    ]
