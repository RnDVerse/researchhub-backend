# Generated by Django 2.2 on 2021-10-05 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0065_auto_20210930_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='access_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization', to='researchhub_access_group.ResearchhubAccessGroup'),
        ),
    ]
