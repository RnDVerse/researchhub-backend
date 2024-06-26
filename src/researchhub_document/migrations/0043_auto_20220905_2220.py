# Generated by Django 2.2 on 2022-09-05 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchhub_document', '0042_auto_20220830_0026'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='researchhubunifieddocument',
            index=models.Index(condition=models.Q(_negated=True, document_type='NOTE'), fields=['document_type'], name='uni_doc_not_note_doc_type_idx'),
        ),
        migrations.AddIndex(
            model_name='researchhubunifieddocument',
            index=models.Index(condition=models.Q(('is_removed', False), models.Q(_negated=True, document_type='NOTE'), ('document_filter__isnull', False)), fields=['document_type'], name='uni_doc_cond_idx'),
        ),
    ]
