# Generated by Django 4.1 on 2024-05-17 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("institution", "0004_institution_openalex_created_date_and_more"),
        ("paper", "0124_workauthorship"),
    ]

    operations = [
        migrations.AddField(
            model_name="workauthorship",
            name="work",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="authorships",
                to="paper.paper",
            ),
        ),
        migrations.AlterField(
            model_name="workauthorship",
            name="institutions",
            field=models.ManyToManyField(
                related_name="authors", to="institution.institution"
            ),
        ),
    ]
