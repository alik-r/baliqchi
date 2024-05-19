# Generated by Django 5.0.6 on 2024-05-19 14:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_incident_acknowledged_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alert",
            name="fingerprint",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="alert",
            name="timestamp",
            field=models.BigIntegerField(default=1716129896167),
        ),
    ]
