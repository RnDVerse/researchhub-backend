# Generated by Django 2.2 on 2020-11-05 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0027_auto_20201104_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='sift_risk_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reply',
            name='sift_risk_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='thread',
            name='sift_risk_score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]