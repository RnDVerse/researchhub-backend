# Generated by Django 2.2 on 2021-06-03 22:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('researchhub_document', '0002_auto_20210603_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researchhubpost',
            name='post_type',
        ),
        migrations.AddField(
            model_name='researchhubpost',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='researchhubpost',
            name='discussion_src',
            field=models.FileField(blank=True, default=None, max_length=512, null=True, upload_to='uploads/post_discussion/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='researchhubpost',
            name='editor_type',
            field=models.CharField(choices=[('CK_EDITOR', 'CK_EDITOR'), ('DRAFT_JS', 'DRAFT_JS')], default='CK_EDITOR', help_text='Editor used to compose the post', max_length=32),
        ),
        migrations.AddField(
            model_name='researchhubpost',
            name='eln_src',
            field=models.FileField(blank=True, default=None, max_length=512, null=True, upload_to='uploads/post_eln/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='researchhubpost',
            name='renderable_text',
            field=models.TextField(blank='true', default=''),
        ),
        migrations.AddField(
            model_name='researchhubpost',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
