# Generated by Django 2.2 on 2022-02-17 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchhub_case', '0010_auto_20220217_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorclaimcase',
            name='target_author_name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
