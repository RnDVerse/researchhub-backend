# Generated by Django 2.2.9 on 2020-01-10 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_list', '0006_auto_20200110_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailrecipient',
            name='next_cursor',
            field=models.IntegerField(default=0),
        ),
    ]