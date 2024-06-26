# Generated by Django 2.2 on 2021-10-06 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0067_auto_20211005_1901'),
        ('researchhub_access_group', '0004_auto_20211005_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to='user.Organization'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='access_type',
            field=models.CharField(choices=[('ADMIN', 'ADMIN'), ('EDITOR', 'EDITOR'), ('VIEWER', 'VIEWER'), ('MEMBER', 'MEMBER'), ('COMMENTER', 'COMMENTER'), ('NO_ACCESS', 'NO_ACCESS')], default='VIEWER', max_length=16),
        ),
        migrations.AlterField(
            model_name='permission',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to=settings.AUTH_USER_MODEL),
        ),
    ]
