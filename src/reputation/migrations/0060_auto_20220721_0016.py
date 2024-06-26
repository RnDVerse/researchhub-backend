# Generated by Django 2.2 on 2022-07-21 00:16

from django.db import migrations, models
import reputation
import django.db.models.deletion
import reputation.related_models.escrow


def create_default_term(apps, schema_editor):
    reputation.related_models.escrow.get_current_bounty_fee()


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0059_auto_20220719_0013'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Term',
            new_name='BountyFee',
        ),
        migrations.RenameField(
            model_name='escrow',
            old_name='term',
            new_name='bounty_fee',
        ),
        migrations.AlterField(
            model_name='escrow',
            name='bounty_fee',
            field=models.ForeignKey(default=reputation.related_models.escrow.get_current_bounty_fee, on_delete=django.db.models.deletion.CASCADE, to='reputation.BountyFee'),
        ),
        migrations.RunPython(create_default_term),
    ]
