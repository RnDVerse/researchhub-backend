# Generated by Django 4.1 on 2024-02-14 18:50

from django.db import migrations, models

def set_closed_fundraises_as_completed(apps, schema_editor):
    Fundraise = apps.get_model("purchase", "Fundraise")
    Fundraise.objects.filter(status="CLOSED").update(status="COMPLETED")

class Migration(migrations.Migration):

    dependencies = [
        ("purchase", "0025_alter_purchase_purchase_type_fundraise"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fundraise",
            name="status",
            field=models.CharField(
                choices=[
                    ("OPEN", "OPEN"),
                    ("CLOSED", "CLOSED"),
                    ("COMPLETED", "COMPLETED"),
                ],
                default="OPEN",
                max_length=32,
            ),
        ),
        migrations.RunPython(set_closed_fundraises_as_completed),
    ]