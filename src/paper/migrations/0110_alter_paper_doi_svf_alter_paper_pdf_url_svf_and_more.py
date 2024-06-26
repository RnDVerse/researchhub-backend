# Generated by Django 4.1 on 2022-12-20 20:53

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("paper", "0109_paper_url_svf_alter_papersubmission_paper_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paper",
            name="doi_svf",
            field=django.contrib.postgres.search.SearchVectorField(
                blank=True, null=True
            ),
        ),
        migrations.AlterField(
            model_name="paper",
            name="pdf_url_svf",
            field=django.contrib.postgres.search.SearchVectorField(
                blank=True, null=True
            ),
        ),
        migrations.AlterField(
            model_name="paper",
            name="url_svf",
            field=django.contrib.postgres.search.SearchVectorField(
                blank=True, null=True
            ),
        ),
    ]
