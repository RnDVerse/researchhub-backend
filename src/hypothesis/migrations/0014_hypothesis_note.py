# Generated by Django 2.2 on 2022-01-27 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_notetemplate'),
        ('hypothesis', '0013_hypothesis_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='hypothesis',
            name='note',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hypothesis', to='note.Note'),
        ),
    ]
