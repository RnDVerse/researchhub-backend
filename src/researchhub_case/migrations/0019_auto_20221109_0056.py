# Generated by Django 2.2 on 2022-11-09 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchhub_case', '0018_auto_20221108_2239'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='externalauthorclaimcase',
            constraint=models.UniqueConstraint(fields=('google_scholar_id', 'requestor'), name='unique_google_scholar_id_claim'),
        ),
    ]
