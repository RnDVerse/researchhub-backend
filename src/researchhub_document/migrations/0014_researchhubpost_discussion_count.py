# Generated by Django 2.2 on 2021-06-11 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchhub_document', '0013_auto_20210604_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchhubpost',
            name='discussion_count',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]