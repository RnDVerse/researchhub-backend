# Generated by Django 2.2 on 2022-06-27 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0104_auto_20220614_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papersubmission',
            name='paper_status',
            field=models.CharField(choices=[('COMPLETE', 'COMPLETE'), ('INITIATED', 'INITIATED'), ('FAILED', 'FAILED'), ('FAILED', 'FAILED_DUPLICATE'), ('FAILED_TIMEOUT', 'FAILED_TIMEOUT'), ('FAILED_DOI', 'FAILED_DOI'), ('PROCESSING', 'PROCESSING'), ('PROCESSING_CROSSREF', 'PROCESSING_CROSSREF'), ('PROCESSING_MANUBOT', 'PROCESSING_MANUBOT'), ('PROCESSING_OPENALEX', 'PROCESSING_OPENALEX'), ('PROCESSING_SEMANTIC_SCHOLAR', 'PROCESSING_SEMANTIC_SCHOLAR'), ('PROCESSING_DOI', 'PROCESSING_DOI')], default='INITIATED', max_length=32),
        ),
    ]