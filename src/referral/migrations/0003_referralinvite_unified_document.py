# Generated by Django 2.2 on 2022-11-03 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('researchhub_document', '0048_researchhubpost_bounty_type'),
        ('referral', '0002_auto_20221103_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='referralinvite',
            name='unified_document',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referral_invites', to='researchhub_document.ResearchhubUnifiedDocument'),
        ),
    ]
