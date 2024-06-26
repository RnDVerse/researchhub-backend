# Generated by Django 2.2 on 2021-08-24 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_auto_20210823_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='notes',
        ),
        migrations.AddField(
            model_name='notecontent',
            name='note',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='note.Note'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='latest_version',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source', to='note.NoteContent'),
        ),
        migrations.AlterField(
            model_name='notecontent',
            name='plain_text',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='notecontent',
            name='src',
            field=models.FileField(blank=True, default=None, max_length=512, null=True, upload_to='note/uploads/%Y/%m/%d'),
        ),
    ]
