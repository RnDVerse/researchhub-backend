# Generated by Django 4.1 on 2023-03-06 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("paper", "0110_alter_paper_doi_svf_alter_paper_pdf_url_svf_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paper",
            name="slug",
            field=models.SlugField(
                blank=True,
                help_text="Slug is automatically generated on a signal, so it is not needed in a form",
                max_length=1024,
            ),
        ),
    ]
