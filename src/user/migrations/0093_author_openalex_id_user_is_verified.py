# Generated by Django 4.1 on 2023-10-11 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0092_remove_verification_file_verification_created_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="openalex_id",
            field=models.CharField(
                blank=True, default=None, max_length=128, null=True, unique=True
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="is_verified",
            field=models.BooleanField(default=False),
        ),
    ]
