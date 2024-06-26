# Generated by Django 4.1 on 2022-11-11 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("researchhub_access_group", "0011_auto_20211020_2256"),
    ]

    operations = [
        migrations.AlterField(
            model_name="permission",
            name="content_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)s_permission",
                to="contenttypes.contenttype",
            ),
        ),
    ]
