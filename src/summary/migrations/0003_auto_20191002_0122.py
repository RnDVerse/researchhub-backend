# Generated by Django 2.2.5 on 2019-10-02 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0002_auto_20191002_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summary',
            name='current',
        ),
        migrations.RemoveField(
            model_name='summary',
            name='paper',
        ),
        migrations.RemoveField(
            model_name='summary',
            name='previous',
        ),
        migrations.AddField(
            model_name='summary',
            name='previous',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next', to='summary.Summary'),
        ),
    ]
