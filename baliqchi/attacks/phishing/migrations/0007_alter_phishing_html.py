# Generated by Django 5.0.6 on 2024-05-19 11:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("phishing", "0006_alter_phishing_html_alter_phishing_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="phishing",
            name="html",
            field=models.FileField(
                blank=True,
                upload_to="baliqchi/attacks/phishing/templates/phishing/c3b1ecb3-e1ac-4f25-9635-85bdf6abbf72/",
            ),
        ),
    ]
