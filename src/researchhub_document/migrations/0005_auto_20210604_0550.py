# Generated by Django 2.2 on 2021-06-04 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('researchhub_document', '0004_researchhubunifieddocument_hubs'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchhubpost',
            name='title',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='researchhubunifieddocument',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_documents', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='researchhubpost',
            name='renderable_text',
            field=models.TextField(blank=True, default=''),
        ),
    ]
