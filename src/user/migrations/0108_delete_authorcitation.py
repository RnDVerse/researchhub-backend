# Generated by Django 4.1 on 2024-05-17 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0107_author_two_year_mean_citedness"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AuthorCitation",
        ),
    ]