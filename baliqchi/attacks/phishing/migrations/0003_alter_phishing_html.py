# Generated by Django 5.0.6 on 2024-05-18 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phishing', '0002_phishing_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phishing',
            name='html',
            field=models.FileField(blank=True, upload_to='baliqchi/staticfiles/phishing_pages/<function uuid4 at 0x7d1d589adbc0>/'),
        ),
    ]
