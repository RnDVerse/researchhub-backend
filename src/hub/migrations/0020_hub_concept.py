# Generated by Django 4.1 on 2023-09-08 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tag", "0004_remove_concept_hub"),
        ("hub", "0019_remove_hubmembership_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="hub",
            name="concept",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="hub",
                to="tag.concept",
            ),
        ),
    ]
