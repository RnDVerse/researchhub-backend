# Generated by Django 2.2 on 2021-10-06 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_notetemplate'),
        ('invite', '0004_auto_20211006_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='noteinvitation',
            name='note',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='invited_users', to='note.Note'),
            preserve_default=False,
        ),
    ]
