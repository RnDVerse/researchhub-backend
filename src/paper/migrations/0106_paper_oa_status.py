# Generated by Django 2.2 on 2022-08-08 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0105_auto_20220627_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='oa_status',
            field=models.CharField(blank=True, default=None, max_length=8, null=True),
        ),
    ]