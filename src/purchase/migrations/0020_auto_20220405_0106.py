# Generated by Django 2.2 on 2022-04-05 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0019_rscexchangerate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase_type',
            field=models.CharField(choices=[('BOOST', 'BOOST'), ('DOI', 'DOI')], max_length=16),
        ),
    ]