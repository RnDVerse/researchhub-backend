# Generated by Django 4.1.13 on 2024-04-22 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("referral", "0005_alter_referralinvite_inviter_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ReferralInvite",
        ),
    ]